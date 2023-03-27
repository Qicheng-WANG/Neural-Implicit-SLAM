import torch
import numpy as np


def keyframe_selection_overlap(self, gt_color, gt_depth, c2w, keyframe_dict, k, N_samples=16, pixels=100):
    """
    Select overlapping keyframes to the current camera observation.

    Args:
        gt_color (tensor): ground truth color image of the current frame.
        gt_depth (tensor): ground truth depth image of the current frame.
        c2w (tensor): camera to world matrix (3*4 or 4*4 both fine).
        keyframe_dict (list): a list containing info for each keyframe.
        k (int): number of overlapping keyframes to select.
        N_samples (int, optional): number of samples/points per ray. Defaults to 16.
        pixels (int, optional): number of pixels to sparsely sample 
            from the image of the current camera. Defaults to 100.
    Returns:
        selected_keyframe_list (list): list of selected keyframe id.
    """
    device = self.device
    H, W, fx, fy, cx, cy = self.H, self.W, self.fx, self.fy, self.cx, self.cy

    rays_o, rays_d, gt_depth, gt_color = get_samples(
        0, H, 0, W, pixels, H, W, fx, fy, cx, cy, c2w, gt_depth, gt_color, self.device)

    gt_depth = gt_depth.reshape(-1, 1)
    gt_depth = gt_depth.repeat(1, N_samples)
    t_vals = torch.linspace(0., 1., steps=N_samples).to(device)
    near = gt_depth*0.8
    far = gt_depth+0.5
    z_vals = near * (1.-t_vals) + far * (t_vals)
    pts = rays_o[..., None, :] + rays_d[..., None, :] * \
        z_vals[..., :, None]  # [N_rays, N_samples, 3]
    vertices = pts.reshape(-1, 3).cpu().numpy()
    list_keyframe = []
    for keyframeid, keyframe in enumerate(keyframe_dict):
        c2w = keyframe['est_c2w'].cpu().numpy()
        w2c = np.linalg.inv(c2w)
        ones = np.ones_like(vertices[:, 0]).reshape(-1, 1)
        homo_vertices = np.concatenate(
            [vertices, ones], axis=1).reshape(-1, 4, 1)  # (N, 4)
        cam_cord_homo = w2c@homo_vertices  # (N, 4, 1)=(4,4)*(N, 4, 1)
        cam_cord = cam_cord_homo[:, :3]  # (N, 3, 1)
        K = np.array([[fx, .0, cx], [.0, fy, cy],
                        [.0, .0, 1.0]]).reshape(3, 3)
        cam_cord[:, 0] *= -1
        uv = K@cam_cord
        z = uv[:, -1:]+1e-5
        uv = uv[:, :2]/z
        uv = uv.astype(np.float32)
        edge = 20
        mask = (uv[:, 0] < W-edge)*(uv[:, 0] > edge) * \
            (uv[:, 1] < H-edge)*(uv[:, 1] > edge)
        mask = mask & (z[:, :, 0] < 0)
        mask = mask.reshape(-1)
        percent_inside = mask.sum()/uv.shape[0]
        list_keyframe.append(
            {'id': keyframeid, 'percent_inside': percent_inside})

    list_keyframe = sorted(
        list_keyframe, key=lambda i: i['percent_inside'], reverse=True)
    selected_keyframe_list = [dic['id']
                                for dic in list_keyframe if dic['percent_inside'] > 0.00]
    selected_keyframe_list = list(np.random.permutation(
        np.array(selected_keyframe_list))[:k])
    return selected_keyframe_list

def random_select(l, k):
    """
    Random select k values from 0..l.

    """
    return list(np.random.permutation(np.array(range(l)))[:min(l, k)])


def render_batch_ray(self, c, decoders, rays_d, rays_o, device, stage, gt_depth=None)：
    pass

def check_information_gain(self,
                           losses_depth_normalized,
                           error_threshold=.1):
    n_nonzero_depth_values = torch.count_nonzero(losses_depth_normalized)
    predictions_below_threshold = torch.logical_and(losses_depth_normalized < error_threshold, losses_depth_normalized > 0.)
    n_predicitions_below_threshold = torch.count_nonzero(predictions_below_threshold, dim=0)
    
    return n_predicitions_below_threshold / n_nonzero_depth_values

def should_add_new_keyframe(self):
    information_gain = check_information_gain(self.prev_scene_model,
                                                self.current_frame_rgb,
                                                self.current_frame_depth,
                                                self.current_frame_pose,
                                                400)
    frames_elapsed = self.current_frame_idx - self.keyframes_indices[-1]

    return information_gain < 0.65 and frames_elapsed > self.sharedData.config['min_frames_elapsed_between_keyframes']