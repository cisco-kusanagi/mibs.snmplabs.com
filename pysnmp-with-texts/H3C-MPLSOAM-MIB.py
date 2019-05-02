#
# PySNMP MIB module H3C-MPLSOAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-MPLSOAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:23:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, ModuleIdentity, Bits, NotificationType, TimeTicks, Integer32, MibIdentifier, ObjectIdentity, Counter32, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "ModuleIdentity", "Bits", "NotificationType", "TimeTicks", "Integer32", "MibIdentifier", "ObjectIdentity", "Counter32", "Gauge32", "Unsigned32")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
h3cMplsOam = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79))
if mibBuilder.loadTexts: h3cMplsOam.setLastUpdated('200703310000Z')
if mibBuilder.loadTexts: h3cMplsOam.setOrganization('Huawei 3Com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cMplsOam.setContactInfo('Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: h3cMplsOam.setDescription('This MIB contains objects to configure OAM module. The Operation, Administration and Maintenance (OAM) is an effective means for decreasing the cost of network maintenance. The MPLS OAM is used to administrate and maintain MPLS.')
class H3cMplsOAMDefectType(TextualConvention, Integer32):
    description = "An indication of the OAM's defect type: 1: dServer, server layer defect; 2: dPeerMe, peer network maintenance entity defect; 3: dLOCV, Loss of Connectivity Verification defect; 4: dTTSIMismatch, Trail Termination Source Identifier Mismatch defect; 5: dTTSIMismerge, Trail Termination Source Identifier Mismerge defect; 6: dExcess, receiving excess rate of CV/FFD; 7: dUnknown, unknown defect in the MPLS network.. 8: rlsn down; 9: dLspDown; 10: MPLS OAM ME; 11: no defect."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("dServer", 1), ("dPeerMe", 2), ("dLOCV", 3), ("dTTSIMismatch", 4), ("dTTSIMismerge", 5), ("dExcess", 6), ("dUnknown", 7), ("dRlsnDown", 8), ("dLspDown", 9), ("dME", 10), ("noDefect", 11))

class H3cMplsOAMDetectFreq(TextualConvention, Integer32):
    description = "An indication of the OAM's frequent type( ITU-T: Y.1711(0402) ): For CV: the frequency is static. The value is 1/s. For FFD: the frequency is set by user. The value can be 10ms, 20ms, 50ms, 100ms, 200ms, 500ms. Any other frequency is wrong. 1: 10ms; 2: 20ms; 3: 50ms; 4: 100ms; 5: 200ms; 6: 500ms; 7: 1000ms(only for cv)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("ffd10ms", 1), ("ffd20ms", 2), ("ffd50ms", 3), ("ffd100ms", 4), ("ffd200ms", 5), ("ffd500ms", 6), ("cv1000ms", 7))

h3cMplsOamScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 1))
h3cMplsOamCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMplsOamCapability.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamCapability.setDescription('Whether OAM is globally capable. false: incapable; true: capable; The default value is incapable.')
h3cMplsOamTrapOpen = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMplsOamTrapOpen.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamTrapOpen.setDescription('Whether OAM trap is globally enabled. false: disable; true: enable; The default value is disable.')
h3cMplsOamTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2))
h3cMplsOamIgrTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1), )
if mibBuilder.loadTexts: h3cMplsOamIgrTable.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrTable.setDescription('This table specifies per-LSP MPLS OAM ingress capability and associated information, such as IgrLspName and IgrDetType.')
h3cMplsOamIgrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1), ).setIndexNames((0, "H3C-MPLSOAM-MIB", "h3cMplsOamIgrIndex"))
if mibBuilder.loadTexts: h3cMplsOamIgrEntry.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrEntry.setDescription('An entry in this table is created by an LSR for every LSP capable of supporting MPLS OAM at ingress.')
h3cMplsOamIgrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: h3cMplsOamIgrIndex.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrIndex.setDescription('This is an unique index for an OAM ingress entry in the OAM table.')
h3cMplsOamIgrLspName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamIgrLspName.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrLspName.setDescription('The name of an LSP. It means the LSP name of the detected LSP.')
h3cMplsOamIgrDetectType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cv", 1), ("ffd", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamIgrDetectType.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrDetectType.setDescription('There are two types of OAM packets, CV and FFD. The CV flow is generated at the source LSR of the LSP with a nominal frequency of 1/s and terminated at the sink LSR of the LSP. FFD provides failure detection option for an LSP independent of the CV based availability model and is not tied to the CV insertion rate. Insertion rates at 1/s or faster may also be used. The CV/FFD packet contains a network-unique identifier (TTSI) so that all types of defects can be detected. 1: CV; 2: FFD.')
h3cMplsOamIgrDetectFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 4), H3cMplsOAMDetectFreq()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamIgrDetectFreq.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrDetectFreq.setDescription("Indication of the OAM's frequent type.")
h3cMplsOamIgrRevType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("private", 1), ("share", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamIgrRevType.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrRevType.setDescription('When an LSP is found to be in defect, the sink LSR of the LSP should send BDI to inform the source LSR of the LSP, the BDI is transferred through the reverse LSP. The type of reverse LSP can be private or shared. If private, then the reverse LSP can be used only by the oam ingress; If shared, the reverse LSP which is shared between many forward LSPs, whose source LSRs are the same and sink LSRs are the same. 1: private; 2: share.')
h3cMplsOamIgrRevLspName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 6), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamIgrRevLspName.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrRevLspName.setDescription('The object indicates the name of the reverse LSP.')
h3cMplsOamIgrLspId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamIgrLspId.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrLspId.setDescription('For ingress, the object indicates the lsp ID of the detected LSP.')
h3cMplsOamIgrEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamIgrEnable.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrEnable.setDescription('Whether one LSP is OAM enable. If disable, LSP is not monitored; If enable, CV/FFD is generated at the source LSR of the LSP and checked at the sink LSR of the LSP, and user can set other configuration. false: The OAM function is disabled on the ingress; true: The OAM function is enabled on the ingress.')
h3cMplsOamIgrDefectType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 9), H3cMplsOAMDefectType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMplsOamIgrDefectType.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrDefectType.setDescription("Indication of the OAM's defect type.")
h3cMplsOamIgrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamIgrRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrRowStatus.setDescription('This object is responsible for managing the creation, deletion and modification of rows, which support active status and CreatAndGo, destroy operation. To create a new row, h3cMplsOamIgrLspName, h3cMplsOamIgrDetectType, h3cMplsOamIgrDetectFreq, h3cMplsOamIgrRevType, h3cMplsOamIgrRevLspName, and h3cMplsOamIgrLspId must be specified.')
h3cMplsOamEgrTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2), )
if mibBuilder.loadTexts: h3cMplsOamEgrTable.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrTable.setDescription('This table specifies per-LSP MPLS OAM capability and associated information, such as DetectType, DetectFrequency.')
h3cMplsOamEgrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1), ).setIndexNames((0, "H3C-MPLSOAM-MIB", "h3cMplsOamEgrIndex"))
if mibBuilder.loadTexts: h3cMplsOamEgrEntry.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrEntry.setDescription('An entry in this table is created by an LSR for every LSP capable of supporting MPLS OAM at egress.')
h3cMplsOamEgrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: h3cMplsOamEgrIndex.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrIndex.setDescription('This is a unique index for an OAM egress entry in the OAM table.')
h3cMplsOamEgrLspName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamEgrLspName.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrLspName.setDescription('The object indicates the name of static LSP at egress.')
h3cMplsOamEgrDetectType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cv", 1), ("ffd", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamEgrDetectType.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrDetectType.setDescription('There are two types of OAM packets, CV and FFD. The CV flow is generated at the source LSR of the LSP with a nominal frequency of 1/s and terminated at the sink LSR of the LSP. FFD provides failure detection option for an LSP independent of the CV based availability model and is not tied to the CV insertion rate. Insertion rates at 1/s or faster may also be used. The CV/FFD packet contains a network-unique identifier (TTSI) so that all types of defects can be detected. 1: CV; 2: FFD.')
h3cMplsOamEgrDetectFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 4), H3cMplsOAMDetectFreq()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamEgrDetectFreq.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrDetectFreq.setDescription("Indication of the OAM's frequent type.")
h3cMplsOamEgrRevType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("private", 1), ("share", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamEgrRevType.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrRevType.setDescription('When an LSP is found to be in defect, the sink LSR of the LSP should send BDI to inform the source LSR of the LSP, the BDI is transferred through the reverse LSP. The type of reverse LSP can be private or shared. If private, then the reverse LSP can be used only when the only LSP in defect; If shared, the reverse LSP, which is shared between many forward LSPs that have the same source LSRs and sink LSRs. 1: private; 2: share.')
h3cMplsOamEgrRevLspName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 6), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamEgrRevLspName.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrRevLspName.setDescription('The object indicates the name of a reverse static-lsp.')
h3cMplsOamEgrLsrId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamEgrLsrId.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrLsrId.setDescription('The object indicates the Ingress LSR ID of the LSP.')
h3cMplsOamEgrLspId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamEgrLspId.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrLspId.setDescription('The object indicates the the Ingress session lsp ID of the detected static-LSP.')
h3cMplsOamEgrEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamEgrEnable.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrEnable.setDescription('Whether one LSP is enabled with OAM. If disable, LSP is not monitored; If enable, CV/FFD is generated at the source LSR of the LSP and checked at the sink LSR of the LSP, and user can set other configuration. false: The OAM function is disabled on the egress; true: The OAM function is enabled on the egress.')
h3cMplsOamEgrDefectType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 10), H3cMplsOAMDefectType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMplsOamEgrDefectType.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrDefectType.setDescription("Indication of the OAM's defect type.")
h3cMplsOamEgrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMplsOamEgrRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrRowStatus.setDescription('This object is responsible for managing the creation, deletion and modification of rows, which support active status and CreatAndGo, destroy operation. To create a new row, h3cMplsOamEgrLspName, h3cMplsOamEgrDetectType, h3cMplsOamEgrDetectFreq, h3cMplsOamEgrRevType, h3cMplsOamEgrRevLspName, h3cMplsOamEgrLsrId and h3cMplsOamEgrLspId must be specified.')
h3cMplsOamNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 3))
h3cMplsOamIgrLSPOutDefect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 3, 1)).setObjects(("H3C-MPLSOAM-MIB", "h3cMplsOamIgrLspName"), ("H3C-MPLSOAM-MIB", "h3cMplsOamIgrDefectType"))
if mibBuilder.loadTexts: h3cMplsOamIgrLSPOutDefect.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrLSPOutDefect.setDescription('This notification is generated when the LSP is found out of the defect state at the LSP ingress.')
h3cMplsOamIgrLSPInDefect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 3, 2)).setObjects(("H3C-MPLSOAM-MIB", "h3cMplsOamIgrLspName"), ("H3C-MPLSOAM-MIB", "h3cMplsOamIgrDefectType"))
if mibBuilder.loadTexts: h3cMplsOamIgrLSPInDefect.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamIgrLSPInDefect.setDescription('This notification is generated when the LSP is found in the defect state at the LSP ingress.')
h3cMplsOamEgrLSPOutDefect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 3, 3)).setObjects(("H3C-MPLSOAM-MIB", "h3cMplsOamEgrLspName"), ("H3C-MPLSOAM-MIB", "h3cMplsOamEgrDefectType"))
if mibBuilder.loadTexts: h3cMplsOamEgrLSPOutDefect.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrLSPOutDefect.setDescription('This notification is generated when the LSP is found out of the defect state at the LSP egress.')
h3cMplsOamEgrLSPInDefect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 3, 4)).setObjects(("H3C-MPLSOAM-MIB", "h3cMplsOamEgrLspName"), ("H3C-MPLSOAM-MIB", "h3cMplsOamEgrDefectType"))
if mibBuilder.loadTexts: h3cMplsOamEgrLSPInDefect.setStatus('current')
if mibBuilder.loadTexts: h3cMplsOamEgrLSPInDefect.setDescription('This notification is generated when the LSP is found in the defect state at the LSP egress.')
mibBuilder.exportSymbols("H3C-MPLSOAM-MIB", h3cMplsOamIgrIndex=h3cMplsOamIgrIndex, h3cMplsOamIgrEnable=h3cMplsOamIgrEnable, h3cMplsOamIgrEntry=h3cMplsOamIgrEntry, h3cMplsOamScalarGroup=h3cMplsOamScalarGroup, h3cMplsOamIgrLspName=h3cMplsOamIgrLspName, h3cMplsOamIgrRevType=h3cMplsOamIgrRevType, h3cMplsOamIgrRevLspName=h3cMplsOamIgrRevLspName, h3cMplsOamEgrDefectType=h3cMplsOamEgrDefectType, h3cMplsOamTrapOpen=h3cMplsOamTrapOpen, h3cMplsOamIgrLSPInDefect=h3cMplsOamIgrLSPInDefect, H3cMplsOAMDetectFreq=H3cMplsOAMDetectFreq, h3cMplsOamEgrDetectType=h3cMplsOamEgrDetectType, h3cMplsOamTable=h3cMplsOamTable, PYSNMP_MODULE_ID=h3cMplsOam, h3cMplsOamEgrEnable=h3cMplsOamEgrEnable, h3cMplsOamIgrDetectFreq=h3cMplsOamIgrDetectFreq, h3cMplsOamCapability=h3cMplsOamCapability, h3cMplsOamEgrDetectFreq=h3cMplsOamEgrDetectFreq, h3cMplsOamEgrRowStatus=h3cMplsOamEgrRowStatus, h3cMplsOamEgrLspName=h3cMplsOamEgrLspName, h3cMplsOamNotifications=h3cMplsOamNotifications, h3cMplsOamEgrIndex=h3cMplsOamEgrIndex, h3cMplsOamEgrLspId=h3cMplsOamEgrLspId, h3cMplsOamEgrLSPOutDefect=h3cMplsOamEgrLSPOutDefect, h3cMplsOamIgrLSPOutDefect=h3cMplsOamIgrLSPOutDefect, h3cMplsOamEgrLsrId=h3cMplsOamEgrLsrId, h3cMplsOamEgrLSPInDefect=h3cMplsOamEgrLSPInDefect, h3cMplsOamIgrDefectType=h3cMplsOamIgrDefectType, h3cMplsOamEgrTable=h3cMplsOamEgrTable, h3cMplsOam=h3cMplsOam, h3cMplsOamIgrDetectType=h3cMplsOamIgrDetectType, h3cMplsOamIgrTable=h3cMplsOamIgrTable, h3cMplsOamEgrEntry=h3cMplsOamEgrEntry, h3cMplsOamEgrRevLspName=h3cMplsOamEgrRevLspName, H3cMplsOAMDefectType=H3cMplsOAMDefectType, h3cMplsOamIgrRowStatus=h3cMplsOamIgrRowStatus, h3cMplsOamIgrLspId=h3cMplsOamIgrLspId, h3cMplsOamEgrRevType=h3cMplsOamEgrRevType)
