# python src/tools/eval_recon.py --rec_mesh output/Replica/room0/mesh/final_mesh_eval_rec.ply --gt_mesh cull_replica_mesh/room0.ply -2d
# python src/tools/eval_recon.py --rec_mesh output/Replica/room1/mesh/final_mesh_eval_rec.ply --gt_mesh cull_replica_mesh/room1.ply -2d
# python src/tools/eval_recon.py --rec_mesh output/Replica/room2/mesh/final_mesh_eval_rec.ply --gt_mesh cull_replica_mesh/room2.ply -2d
# python src/tools/eval_recon.py --rec_mesh output/Replica/office0/mesh/final_mesh_eval_rec.ply --gt_mesh cull_replica_mesh/office0.ply -2d
# python src/tools/eval_recon.py --rec_mesh output/Replica/office1/mesh/final_mesh_eval_rec.ply --gt_mesh cull_replica_mesh/office1.ply -2d
# python src/tools/eval_recon.py --rec_mesh output/Replica/office2/mesh/final_mesh_eval_rec.ply --gt_mesh cull_replica_mesh/office2.ply -2d
# python src/tools/eval_recon.py --rec_mesh output/Replica/office3/mesh/final_mesh_eval_rec.ply --gt_mesh cull_replica_mesh/office3.ply -2d
# python src/tools/eval_recon.py --rec_mesh output/Replica/office4/mesh/final_mesh_eval_rec.ply --gt_mesh cull_replica_mesh/office4.ply -2d

python src/tools/eval_recon.py --rec_mesh output_imap/Replica/room0_key00global+weight+12+rendered/mesh/final_mesh_eval_rec_scaled.ply --gt_mesh cull_replica_mesh/room0.ply -2d --save
python src/tools/eval_recon.py --rec_mesh output_imap/Replica/room1_key00global+weight+12+rendered/mesh/final_mesh_eval_rec_scaled.ply --gt_mesh cull_replica_mesh/room1.ply -2d --save
python src/tools/eval_recon.py --rec_mesh output_imap/Replica/room2_key00global+weight+12+rendered/mesh/final_mesh_eval_rec_scaled.ply --gt_mesh cull_replica_mesh/room2.ply -2d --save
python src/tools/eval_recon.py --rec_mesh output_imap/Replica/office0_key00global+weight+12+rendered/mesh/final_mesh_eval_rec_scaled.ply --gt_mesh cull_replica_mesh/office0.ply -2d --save
python src/tools/eval_recon.py --rec_mesh output_imap/Replica/office1_key00global+weight+12+rendered/mesh/final_mesh_eval_rec_scaled.ply --gt_mesh cull_replica_mesh/office1.ply -2d --save
python src/tools/eval_recon.py --rec_mesh output_imap/Replica/office2_key00global+weight+12+rendered/mesh/final_mesh_eval_rec_scaled.ply --gt_mesh cull_replica_mesh/office2.ply -2d --save
python src/tools/eval_recon.py --rec_mesh output_imap/Replica/office3_key00global+weight+12+rendered/mesh/final_mesh_eval_rec_scaled.ply --gt_mesh cull_replica_mesh/office3.ply -2d --save
python src/tools/eval_recon.py --rec_mesh output_imap/Replica/office4_key00global+weight+12+rendered/mesh/final_mesh_eval_rec_scaled.ply --gt_mesh cull_replica_mesh/office4.ply -2d --save

# python src/tools/eval_recon.py --rec_mesh output_imap/scannet_8layer/scans/scene0000_00/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0000_00/scene0000_00_vh_clean.ply -3d --save
# python src/tools/eval_recon.py --rec_mesh output_imap/scannet_8layer/scans/scene0059_00/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0059_00/scene0059_00_vh_clean.ply -3d --save
# python src/tools/eval_recon.py --rec_mesh output_imap/scannet_8layer/scans/scene0106_00/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0106_00/scene0106_00_vh_clean.ply -3d --save
# python src/tools/eval_recon.py --rec_mesh output_imap/scannet_8layer/scans/scene0169_00/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0169_00/scene0169_00_vh_clean.ply -3d --save
# python src/tools/eval_recon.py --rec_mesh output_imap/scannet_8layer/scans/scene0181_00/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0181_00/scene0181_00_vh_clean.ply -3d --save
# python src/tools/eval_recon.py --rec_mesh output_imap/scannet_8layer/scans/scene0207_00/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0207_00/scene0207_00_vh_clean.ply -3d --save

# python src/tools/eval_recon.py --rec_mesh output_imap/scannet/scans/scene0000_00_key/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0000_00/scene0000_00_vh_clean.ply -3d --save
# python src/tools/eval_recon.py --rec_mesh output_imap/scannet/scans/scene0059_00_key/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0059_00/scene0059_00_vh_clean.ply -3d --save
# python src/tools/eval_recon.py --rec_mesh output_imap/scannet/scans/scene0106_00_key/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0106_00/scene0106_00_vh_clean.ply -3d --save
# python src/tools/eval_recon.py --rec_mesh output_imap/scannet/scans/scene0169_00_key/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0169_00/scene0169_00_vh_clean.ply -3d --save
# python src/tools/eval_recon.py --rec_mesh output_imap/scannet/scans/scene0181_00_key/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0181_00/scene0181_00_vh_clean.ply -3d --save
# python src/tools/eval_recon.py --rec_mesh output_imap/scannet/scans/scene0207_00_key/mesh/final_mesh.ply --gt_mesh Datasets/scannet/scans/scene0207_00/scene0207_00_vh_clean.ply -3d --save

# python src/tools/eval_recon.py --rec_mesh output/TUM_RGBD/rgbd_dataset_freiburg1_desk/mesh/final_mesh.ply --gt_mesh Datasets/TUM_RGBD/rgbd_dataset_freiburg1_desk/scene0207_00_vh_clean.ply -2d