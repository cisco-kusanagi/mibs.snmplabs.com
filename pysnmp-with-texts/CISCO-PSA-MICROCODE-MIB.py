#
# PySNMP MIB module CISCO-PSA-MICROCODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PSA-MICROCODE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:10:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalDescr, entPhysicalIndex, entPhysicalName = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalDescr", "entPhysicalIndex", "entPhysicalName")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Counter64, Counter32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, MibIdentifier, NotificationType, Bits, TimeTicks, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Counter32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "MibIdentifier", "NotificationType", "Bits", "TimeTicks", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoPsaMicrocodeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 259))
ciscoPsaMicrocodeMIB.setRevisions(('2002-06-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPsaMicrocodeMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPsaMicrocodeMIB.setLastUpdated('200206180000Z')
if mibBuilder.loadTexts: ciscoPsaMicrocodeMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPsaMicrocodeMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134-1706 USA Tel: +1 800 553-NETS E-mail: gsr-netman@cisco.com')
if mibBuilder.loadTexts: ciscoPsaMicrocodeMIB.setDescription('Cisco PSA Microcode MIB - Overview The PSA is the Packet Switching ASIC used in module like engine 2(E2) line cards in GSR for IP and MPLS packets forwarding. The PSA performs IP and MPLS packet forwarding at 4 Mpps. The list of features supported by the PSA includes (but is not limited to): - Input and Output ACLs - Frame Relay Switching - PIRC - MPLS VPN - BGP policy accounting - IP packet coloring - Sampled Net flow - ATM over MPLS. - Source MAC Accounting. - Unicast RPF Note that all the features are not supported simultaneously on a module. Each microcode bundle/set can support one or a limited number of the features listed above. Each feature has a priority. When a feature (ACL, Sampled NetFlow) is enabled through the CLI, the higher priority feature will take precedence over the lower priority feature. The microcode for the lower priority is removed and cleaned up. The higher priority microcode will be loaded. Later, if the higher priority feature is removed, the lower priority microcode will be loaded again. This MIB contains information about the microcode bundles on modules like E2 Line Cards(LC) in GSR. Since microcode reload is a service interrupting event, this MIB also defines a notification to inform management stations that such an event has taken place. ')
ciscoPsaMicrocodeMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 0))
ciscoPsaMicrocodeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 1))
ciscoPsaMicrocodeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 2))
cpmcModulePsa = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1))
cpmcBundle = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2))
cpmcNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 3))
class PsaMicrocodeBundleId(TextualConvention, Integer32):
    description = 'The identity of a PSA microcode bundle. The current microcode bundles are: unknown(1): Unknown Bundle. There will be no entry associated with this value in the cpmcBundleTable. none(2): This value is used by cpmcModulePsaPrevBundleId object till the first micrcode reload occurs on the psa. There will be no entry associated with this value in the cpmcBundleTable. vanillaPOS(3): POS Vanilla vanillaGE(4): GE Vanilla vanillaInuit(5): Inuit Vanilla vanillaTaz(6): TAZ Vanilla pircPOS(7): POS Per Interface Rate Control pircGE(8): GE Per Interface Rate Control uRPFPOS(9): POS Unicast Reverse Path Forwarding vrfSelectionPOS(10): POS VRF Selection bgppaPOS(11): POS BGP Policy Accounting bgppaGE(12): GE BGP Policy Accounting ipColorPOS(13): POS IP Coloring inputAcl128POS(14): POS 128 Line Input ACL inputAcl128GE(15): GE 128 Line Input ACL outputAcl128POS(16): POS 128 Line Output ACL outputAcl128GE(17): GE 128 Line Output ACL inputAcl448POS(18): POS 448 Line Input ACL inputAcl448GE(19): GE 448 Line Input ACL outputAcl448POS(20): POS 448 Line Output ACL outputAcl448GE(21): GE 448 Line Output ACL serverCard(22): Server Card eoMplsGE(23): GE Ethernet over MPLS frtpPOS(24): POS Frame Relay Traffic Policing outputAclATM(25): ATM Output ACL inputAcl128Taz(26): TAZ 128 Line Input ACL vrfSelectionGE(27): GE VRF Selection uRPFGE(28): GE Unicast Reverse Path Forwarding cscGE(29): GE Carrier Supporting Carriers linkBundleSMPOS(30): POS Link Bundle Single Mode linkBundleDMPOS(31): POS Link Bundle Double Mode linkBundleSMGE(32): GE Link Bundle Single Mode linkBundleDMGE(33): GE Link Bundle Double Mode '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33))
    namedValues = NamedValues(("unknown", 1), ("none", 2), ("vanillaPOS", 3), ("vanillaGE", 4), ("vanillaInuit", 5), ("vanillaTaz", 6), ("pircPOS", 7), ("pircGE", 8), ("uRPFPOS", 9), ("vrfSelectionPOS", 10), ("bgppaPOS", 11), ("bgppaGE", 12), ("ipColorPOS", 13), ("inputAcl128POS", 14), ("inputAcl128GE", 15), ("outputAcl128POS", 16), ("outputAcl128GE", 17), ("inputAcl448POS", 18), ("inputAcl448GE", 19), ("outputAcl448POS", 20), ("outputAcl448GE", 21), ("serverCard", 22), ("eoMplsGE", 23), ("frtpPOS", 24), ("outputAclATM", 25), ("inputAcl128Taz", 26), ("vrfSelectionGE", 27), ("uRPFGE", 28), ("cscGE", 29), ("linkBundleSMPOS", 30), ("linkBundleDMPOS", 31), ("linkBundleSMGE", 32), ("linkBundleDMGE", 33))

class PsaMicrocodeFeatures(TextualConvention, Bits):
    description = 'The list of features supported on a PSA microcode bundle. The current list of features are: basicIpForwarding(0): Basic IP Forwarding basicMplsSwitching(1): Basic MPLS Switching frameRelaySwitching(2): Frame Relay Switching eAFrSwitching(3): Extended Addressing FR Switching frtp(4): Frame Relay Traffic Policing pirc(5): PIRC vrfSelection(6): VRF Selection uRPF(7): Unicast RPF inputAcl128(8): 128 Line Input ACLs outputAcl128(9): 128 Line Output ACLs inputAcl448(10): 448 Line Input ACLs outputAcl448(11): 448 Line Output ACLs. sampledNetflow(12): Sampled Netflow ipMarking(13): IP Marking bgppa(14): BGP Policy Accounting uti(15): Universal Transport Interface mplsVpn(16): MPLS VPN eoMpls(17): Ethernet over MPLS atmoMpls(18): ATM over MPLS csc(19): Carrier Supporting Carriers multicast(20): Multicast perPacketLoadBalancing(21): Per Packet Load Balancing sourceMacAccounting(22): Source MAC Accounting frSubVrf(23): FR per-subinterface VRF processing serverCard(24): Server Card mplsSNF(25): MPLS aware Sampled Netflow linkBundle(26): Link Bundle atomDisposition(27): AToM Disposition '
    status = 'current'
    namedValues = NamedValues(("basicIpForwarding", 0), ("basicMplsSwitching", 1), ("frameRelaySwitching", 2), ("eAFrSwitching", 3), ("frtp", 4), ("pirc", 5), ("vrfSelection", 6), ("uRPF", 7), ("inputAcl128", 8), ("outputAcl128", 9), ("inputAcl448", 10), ("outputAcl448", 11), ("sampledNetflow", 12), ("ipMarking", 13), ("bgppa", 14), ("uti", 15), ("mplsVpn", 16), ("eoMpls", 17), ("atmoMpls", 18), ("csc", 19), ("multicast", 20), ("perPacketLoadBalancing", 21), ("sourceMacAccounting", 22), ("frSubVrf", 23), ("serverCard", 24), ("mplsSNF", 25), ("linkBundle", 26), ("atomDisposition", 27))

cpmcModulePsaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1), )
if mibBuilder.loadTexts: cpmcModulePsaTable.setStatus('current')
if mibBuilder.loadTexts: cpmcModulePsaTable.setDescription('A table providing the microcode bundle information of those modules which contains PSA (Ex: engine 2 line cards in GSR).')
cpmcModulePsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cpmcModulePsaEntry.setStatus('current')
if mibBuilder.loadTexts: cpmcModulePsaEntry.setDescription('Entries providing PSA microcode bundle information of those entities of type PhysicalClass module(9) and contain PSA.')
cpmcModulePsaCurrBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 1), PsaMicrocodeBundleId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmcModulePsaCurrBundleId.setStatus('current')
if mibBuilder.loadTexts: cpmcModulePsaCurrBundleId.setDescription('The identity of the microcode bundle currently loaded on the PSA of the module identified by entPhysicalIndex.')
cpmcModulePsaPrevBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 2), PsaMicrocodeBundleId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmcModulePsaPrevBundleId.setStatus('current')
if mibBuilder.loadTexts: cpmcModulePsaPrevBundleId.setDescription("The identity of the microcode bundle previously loaded on the PSA of the module identified by entPhysicalIndex. Till the first microcode reload is performed on the module, the value will be 'none(2)'.")
cpmcModulePsaFeaturesEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 3), PsaMicrocodeFeatures()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmcModulePsaFeaturesEnabled.setStatus('current')
if mibBuilder.loadTexts: cpmcModulePsaFeaturesEnabled.setDescription('The list of features newly enabled due to the loading of the microcode bundle identified by cpmcModulePsaCurrBundleId. ')
cpmcModulePsaFeaturesDisabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 4), PsaMicrocodeFeatures()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmcModulePsaFeaturesDisabled.setStatus('current')
if mibBuilder.loadTexts: cpmcModulePsaFeaturesDisabled.setDescription('The list of features disabled because of the unloading of microcode bundle identified by cpmcModulePsaPrevBundleId and loading of the microcode bundle identified by cpmcModulePsaCurrBundleId.')
cpmcBundleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1), )
if mibBuilder.loadTexts: cpmcBundleTable.setStatus('current')
if mibBuilder.loadTexts: cpmcBundleTable.setDescription('A table of PSA microcode bundle features.')
cpmcBundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-PSA-MICROCODE-MIB", "cpmcBundleId"))
if mibBuilder.loadTexts: cpmcBundleEntry.setStatus('current')
if mibBuilder.loadTexts: cpmcBundleEntry.setDescription('Details the features of a microcode bundle.')
cpmcBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1, 1, 1), PsaMicrocodeBundleId())
if mibBuilder.loadTexts: cpmcBundleId.setStatus('current')
if mibBuilder.loadTexts: cpmcBundleId.setDescription("The identity of the PSA microcode bundle. This object value can't be unknown(1) or none(2).")
cpmcBundleFeatures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1, 1, 2), PsaMicrocodeFeatures()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmcBundleFeatures.setStatus('current')
if mibBuilder.loadTexts: cpmcBundleFeatures.setDescription('The list of features supported by microcode bundle identified by cpmcBundleId.')
cpmcNotifEnables = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpmcNotifEnables.setStatus('current')
if mibBuilder.loadTexts: cpmcNotifEnables.setDescription('This variable indicates whether the system produces the ciscoPsaMicrocodeReload notification. A false value will prevent PSA microcode reload notifications from being generated by the system.')
ciscoPsaMicrocodeReload = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 259, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalDescr"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaCurrBundleId"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaPrevBundleId"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesEnabled"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesDisabled"))
if mibBuilder.loadTexts: ciscoPsaMicrocodeReload.setStatus('current')
if mibBuilder.loadTexts: ciscoPsaMicrocodeReload.setDescription('A ciscoPsaMicrocodeReload notification is generated when a PSA microcode reload occurs..')
ciscoPsaMicrocodeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 1))
ciscoPsaMicrocodeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 2))
ciscoPsaMicrocodeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 1, 1)).setObjects(("CISCO-PSA-MICROCODE-MIB", "ciscoPsaMicrocodeParamsGroup"), ("CISCO-PSA-MICROCODE-MIB", "ciscoPsaMicrocodeNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsaMicrocodeMIBCompliance = ciscoPsaMicrocodeMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoPsaMicrocodeMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO-PSA-MICROCODE-MIB.')
ciscoPsaMicrocodeParamsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 2, 1)).setObjects(("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaCurrBundleId"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaPrevBundleId"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesEnabled"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesDisabled"), ("CISCO-PSA-MICROCODE-MIB", "cpmcBundleFeatures"), ("CISCO-PSA-MICROCODE-MIB", "cpmcNotifEnables"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsaMicrocodeParamsGroup = ciscoPsaMicrocodeParamsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoPsaMicrocodeParamsGroup.setDescription('A collection of objects providing PSA microcode monitoring.')
ciscoPsaMicrocodeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 2, 2)).setObjects(("CISCO-PSA-MICROCODE-MIB", "ciscoPsaMicrocodeReload"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsaMicrocodeNotifGroup = ciscoPsaMicrocodeNotifGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoPsaMicrocodeNotifGroup.setDescription('A collection of notifications generated by the devices supporting this MIB.')
mibBuilder.exportSymbols("CISCO-PSA-MICROCODE-MIB", PsaMicrocodeBundleId=PsaMicrocodeBundleId, cpmcBundleId=cpmcBundleId, cpmcModulePsaCurrBundleId=cpmcModulePsaCurrBundleId, ciscoPsaMicrocodeMIB=ciscoPsaMicrocodeMIB, cpmcModulePsaPrevBundleId=cpmcModulePsaPrevBundleId, ciscoPsaMicrocodeMIBGroups=ciscoPsaMicrocodeMIBGroups, cpmcBundleEntry=cpmcBundleEntry, cpmcBundleTable=cpmcBundleTable, cpmcModulePsaTable=cpmcModulePsaTable, ciscoPsaMicrocodeParamsGroup=ciscoPsaMicrocodeParamsGroup, cpmcNotif=cpmcNotif, ciscoPsaMicrocodeNotifGroup=ciscoPsaMicrocodeNotifGroup, cpmcModulePsa=cpmcModulePsa, ciscoPsaMicrocodeMIBNotifs=ciscoPsaMicrocodeMIBNotifs, cpmcBundle=cpmcBundle, cpmcModulePsaEntry=cpmcModulePsaEntry, cpmcModulePsaFeaturesDisabled=cpmcModulePsaFeaturesDisabled, ciscoPsaMicrocodeMIBCompliances=ciscoPsaMicrocodeMIBCompliances, ciscoPsaMicrocodeMIBObjects=ciscoPsaMicrocodeMIBObjects, cpmcBundleFeatures=cpmcBundleFeatures, cpmcNotifEnables=cpmcNotifEnables, PsaMicrocodeFeatures=PsaMicrocodeFeatures, ciscoPsaMicrocodeMIBCompliance=ciscoPsaMicrocodeMIBCompliance, ciscoPsaMicrocodeMIBConformance=ciscoPsaMicrocodeMIBConformance, cpmcModulePsaFeaturesEnabled=cpmcModulePsaFeaturesEnabled, ciscoPsaMicrocodeReload=ciscoPsaMicrocodeReload, PYSNMP_MODULE_ID=ciscoPsaMicrocodeMIB)
