/- Prime Front scoped axiom audit; original TfptCarrier namespaces retained.
Finite/conditional formal statements do not establish RH. -/
import TfptCarrier.AntiAliasExact
import TfptCarrier.ArfSpinorCompiler
import TfptCarrier.CellCocycle
import TfptCarrier.Check32
import TfptCarrier.CofinalCurrent
import TfptCarrier.CofinalEnvelope
import TfptCarrier.CofinalPredefinition
import TfptCarrier.CofinalWeil
import TfptCarrier.DeltaOneNoGo
import TfptCarrier.DenseWeilCore
import TfptCarrier.EulerPick
import TfptCarrier.ExcessSkeleton
import TfptCarrier.GradeNoGo
import TfptCarrier.GramCompactness
import TfptCarrier.JetSumRules
import TfptCarrier.KreinDefect
import TfptCarrier.MatchedPin
import TfptCarrier.MomentLaurent
import TfptCarrier.NFClosure
import TfptCarrier.PacketRM14
import TfptCarrier.ParityLemma
import TfptCarrier.ParityWeightLaws
import TfptCarrier.PinchIdentity
import TfptCarrier.PinningLemma
import TfptCarrier.PositiveC2Lift
import TfptCarrier.PositiveDescentMaster
import TfptCarrier.Radius4Algebra
import TfptCarrier.SVSkeleton
import TfptCarrier.SectorPositiveDescent
import TfptCarrier.SineGramKeystone
import TfptCarrier.SpacingProduct
import TfptCarrier.SpectralBalance
import TfptCarrier.TraceLedger
import TfptCarrier.WallCofinalComposition
import TfptCarrier.WallLadderChecker
import TfptCarrier.WeilDictionary
#print axioms TfptCarrier.CofinalPredefinition.cofinal_weil_for_fixed_idx
#print axioms TfptCarrier.CofinalPredefinition.cofinal_weil_predefined
#print axioms TfptCarrier.CofinalPredefinition.old_api_accepts_sign_mined_idx
#print axioms TfptCarrier.CofinalPredefinition.signMinedIndex_not_familyNoninterfering
#print axioms TfptCarrier.CofinalPredefinition.constantizedSelector_familyNoninterfering
#print axioms TfptCarrier.CofinalPredefinition.constantizedSelector_agrees
#print axioms TfptCarrier.EulerPick.pick_entry_decomposition
#print axioms TfptCarrier.EulerPick.pickMatrix_entry_eq_gram_sum
#print axioms TfptCarrier.EulerPick.pickForm_nonneg
#print axioms TfptCarrier.EulerPick.pickMatrix_posSemidef
#print axioms TfptCarrier.EulerPick.pickMatrix_svNodes_posSemidef
#print axioms TfptCarrier.DeltaOneNoGo.toeplitz_deltaOneMoment
#print axioms TfptCarrier.DeltaOneNoGo.allOnes_posSemidef
#print axioms TfptCarrier.DeltaOneNoGo.allOnes_det_eq_zero
#print axioms TfptCarrier.DeltaOneNoGo.allOnes_not_posDef
#print axioms TfptCarrier.DeltaOneNoGo.caratheodoryDeltaOne_pos
#print axioms TfptCarrier.DeltaOneNoGo.delta_one_no_go
#print axioms TfptCarrier.ParityLemma.tendsto_secular_atTop
#print axioms TfptCarrier.ParityLemma.tendsto_secular_atBot
#print axioms TfptCarrier.ParityLemma.sign_constant_of_no_zero
#print axioms TfptCarrier.ParityLemma.exists_zero_of_pos_pos
#print axioms TfptCarrier.ParityLemma.exists_zero_of_same_sign
#print axioms TfptCarrier.ParityLemma.exists_zero_adjacent
#print axioms TfptCarrier.ParityLemma.parity_of_alternating
#print axioms TfptCarrier.ParityLemma.zero_count_odd_of_pos_pos
#print axioms TfptCarrier.ParityLemma.zero_count_even_of_pos_neg
#print axioms TfptCarrier.ParityLemma.zero_count_even_iff_opposite_residues
#print axioms TfptCarrier.SVSkeleton.svNode_mem_Ioc
#print axioms TfptCarrier.SVSkeleton.svNode_strictAnti
#print axioms TfptCarrier.SVSkeleton.svNode_tendsto_one
#print axioms TfptCarrier.SVSkeleton.sv_implies_rh
#print axioms TfptCarrier.SVSkeleton.skeleton_inhabited
#print axioms TfptCarrier.SVSkeleton.skeleton_not_unconditional
#print axioms TfptCarrier.Radius4Algebra.w_eq_y_one_sub_y
#print axioms TfptCarrier.Radius4Algebra.diagonal_identity
#print axioms TfptCarrier.Radius4Algebra.det_factor
#print axioms TfptCarrier.Radius4Algebra.wOnLine_nonneg
#print axioms TfptCarrier.Radius4Algebra.wOnLine_le_quarter
#print axioms TfptCarrier.Radius4Algebra.w_onLine_eq
#print axioms TfptCarrier.Radius4Algebra.matched_w
#print axioms TfptCarrier.Radius4Algebra.matched_excess_pos
#print axioms TfptCarrier.Radius4Algebra.partner_w
#print axioms TfptCarrier.Radius4Algebra.partner_weight_sum
#print axioms TfptCarrier.MatchedPin.vRate_eq_four_w
#print axioms TfptCarrier.MatchedPin.matched_y
#print axioms TfptCarrier.MatchedPin.matched_y_conj
#print axioms TfptCarrier.MatchedPin.matched_weight_sum
#print axioms TfptCarrier.MatchedPin.matched_y_re
#print axioms TfptCarrier.MatchedPin.matched_v
#print axioms TfptCarrier.MatchedPin.matched_v_gt_one
#print axioms TfptCarrier.MatchedPin.onLine_y_v
#print axioms TfptCarrier.MatchedPin.onLine_rate_pos
#print axioms TfptCarrier.MatchedPin.onLine_rate_le_one
#print axioms TfptCarrier.NFClosure.contractionKernel_mem_Icc
#print axioms TfptCarrier.NFClosure.eigenvalues_mem_Icc
#print axioms TfptCarrier.NFClosure.det_factor_vieta
#print axioms TfptCarrier.NFClosure.det_factor_kernel
#print axioms TfptCarrier.NFClosure.sum_pow_le_trace
#print axioms TfptCarrier.NFClosure.log_inv_one_sub_le
#print axioms TfptCarrier.NFClosure.nf_implies_rh
#print axioms TfptCarrier.NFClosure.nfSkeleton_inhabited
#print axioms TfptCarrier.NFClosure.nfSkeleton_not_unconditional
#print axioms TfptCarrier.SpacingProduct.nodal_erase_wronskian
#print axioms TfptCarrier.SpacingProduct.spacing_product_cleared
#print axioms TfptCarrier.SpacingProduct.spacing_product
#print axioms TfptCarrier.SpacingProduct.fderivWeight_ne_zero
#print axioms TfptCarrier.JetSumRules.spacing_two
#print axioms TfptCarrier.JetSumRules.sum_rule_first
#print axioms TfptCarrier.JetSumRules.sum_rule_second
#print axioms TfptCarrier.JetSumRules.sum_rule_jet
#print axioms TfptCarrier.JetSumRules.sum_rule_jet_second
#print axioms TfptCarrier.JetSumRules.jet_sum_rules_conditional
#print axioms TfptCarrier.JetSumRules.jetSkeleton_inhabited
#print axioms TfptCarrier.JetSumRules.jetSkeleton_not_unconditional
#print axioms TfptCarrier.PinchIdentity.defect_identity
#print axioms TfptCarrier.PinchIdentity.defect_sum_nonneg
#print axioms TfptCarrier.PinchIdentity.sg_le_one
#print axioms TfptCarrier.PinchIdentity.one_sub_div_le_sg
#print axioms TfptCarrier.PinchIdentity.pinch
#print axioms TfptCarrier.SpectralBalance.tf_ge_one
#print axioms TfptCarrier.SpectralBalance.tf_le_card
#print axioms TfptCarrier.SpectralBalance.trace_loop_identity
#print axioms TfptCarrier.SpectralBalance.chi_cap
#print axioms TfptCarrier.SpectralBalance.enclosure_lower
#print axioms TfptCarrier.SpectralBalance.secular_enclosure
#print axioms TfptCarrier.MomentLaurent.y_mul_S
#print axioms TfptCarrier.MomentLaurent.secular_dictionary
#print axioms TfptCarrier.MomentLaurent.geom_remainder
#print axioms TfptCarrier.MomentLaurent.T_laurent
#print axioms TfptCarrier.MomentLaurent.moment_laurent_law
#print axioms TfptCarrier.MomentLaurent.z_mul_one_sub_z_le_quarter
#print axioms TfptCarrier.MomentLaurent.quarter_cap_algebra
#print axioms TfptCarrier.MomentLaurent.quarter_cap_bound
