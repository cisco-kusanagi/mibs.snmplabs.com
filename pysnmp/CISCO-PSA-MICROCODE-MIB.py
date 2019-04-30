#
# PySNMP MIB module CISCO-PSA-MICROCODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PSA-MICROCODE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, entPhysicalDescr, entPhysicalName = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalDescr", "entPhysicalName")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Gauge32, Counter64, MibIdentifier, Integer32, ObjectIdentity, iso, ModuleIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "Counter64", "MibIdentifier", "Integer32", "ObjectIdentity", "iso", "ModuleIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoPsaMicrocodeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 259))
ciscoPsaMicrocodeMIB.setRevisions(('2002-06-18 00:00',))
if mibBuilder.loadTexts: ciscoPsaMicrocodeMIB.setLastUpdated('200206180000Z')
if mibBuilder.loadTexts: ciscoPsaMicrocodeMIB.setOrganization('Cisco Systems, Inc.')
ciscoPsaMicrocodeMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 0))
ciscoPsaMicrocodeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 1))
ciscoPsaMicrocodeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 2))
cpmcModulePsa = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1))
cpmcBundle = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2))
cpmcNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 3))
class PsaMicrocodeBundleId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33))
    namedValues = NamedValues(("unknown", 1), ("none", 2), ("vanillaPOS", 3), ("vanillaGE", 4), ("vanillaInuit", 5), ("vanillaTaz", 6), ("pircPOS", 7), ("pircGE", 8), ("uRPFPOS", 9), ("vrfSelectionPOS", 10), ("bgppaPOS", 11), ("bgppaGE", 12), ("ipColorPOS", 13), ("inputAcl128POS", 14), ("inputAcl128GE", 15), ("outputAcl128POS", 16), ("outputAcl128GE", 17), ("inputAcl448POS", 18), ("inputAcl448GE", 19), ("outputAcl448POS", 20), ("outputAcl448GE", 21), ("serverCard", 22), ("eoMplsGE", 23), ("frtpPOS", 24), ("outputAclATM", 25), ("inputAcl128Taz", 26), ("vrfSelectionGE", 27), ("uRPFGE", 28), ("cscGE", 29), ("linkBundleSMPOS", 30), ("linkBundleDMPOS", 31), ("linkBundleSMGE", 32), ("linkBundleDMGE", 33))

class PsaMicrocodeFeatures(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("basicIpForwarding", 0), ("basicMplsSwitching", 1), ("frameRelaySwitching", 2), ("eAFrSwitching", 3), ("frtp", 4), ("pirc", 5), ("vrfSelection", 6), ("uRPF", 7), ("inputAcl128", 8), ("outputAcl128", 9), ("inputAcl448", 10), ("outputAcl448", 11), ("sampledNetflow", 12), ("ipMarking", 13), ("bgppa", 14), ("uti", 15), ("mplsVpn", 16), ("eoMpls", 17), ("atmoMpls", 18), ("csc", 19), ("multicast", 20), ("perPacketLoadBalancing", 21), ("sourceMacAccounting", 22), ("frSubVrf", 23), ("serverCard", 24), ("mplsSNF", 25), ("linkBundle", 26), ("atomDisposition", 27))

cpmcModulePsaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1), )
if mibBuilder.loadTexts: cpmcModulePsaTable.setStatus('current')
cpmcModulePsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cpmcModulePsaEntry.setStatus('current')
cpmcModulePsaCurrBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 1), PsaMicrocodeBundleId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmcModulePsaCurrBundleId.setStatus('current')
cpmcModulePsaPrevBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 2), PsaMicrocodeBundleId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmcModulePsaPrevBundleId.setStatus('current')
cpmcModulePsaFeaturesEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 3), PsaMicrocodeFeatures()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmcModulePsaFeaturesEnabled.setStatus('current')
cpmcModulePsaFeaturesDisabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 4), PsaMicrocodeFeatures()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmcModulePsaFeaturesDisabled.setStatus('current')
cpmcBundleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1), )
if mibBuilder.loadTexts: cpmcBundleTable.setStatus('current')
cpmcBundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-PSA-MICROCODE-MIB", "cpmcBundleId"))
if mibBuilder.loadTexts: cpmcBundleEntry.setStatus('current')
cpmcBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1, 1, 1), PsaMicrocodeBundleId())
if mibBuilder.loadTexts: cpmcBundleId.setStatus('current')
cpmcBundleFeatures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1, 1, 2), PsaMicrocodeFeatures()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpmcBundleFeatures.setStatus('current')
cpmcNotifEnables = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpmcNotifEnables.setStatus('current')
ciscoPsaMicrocodeReload = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 259, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalDescr"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaCurrBundleId"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaPrevBundleId"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesEnabled"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesDisabled"))
if mibBuilder.loadTexts: ciscoPsaMicrocodeReload.setStatus('current')
ciscoPsaMicrocodeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 1))
ciscoPsaMicrocodeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 2))
ciscoPsaMicrocodeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 1, 1)).setObjects(("CISCO-PSA-MICROCODE-MIB", "ciscoPsaMicrocodeParamsGroup"), ("CISCO-PSA-MICROCODE-MIB", "ciscoPsaMicrocodeNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsaMicrocodeMIBCompliance = ciscoPsaMicrocodeMIBCompliance.setStatus('current')
ciscoPsaMicrocodeParamsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 2, 1)).setObjects(("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaCurrBundleId"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaPrevBundleId"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesEnabled"), ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesDisabled"), ("CISCO-PSA-MICROCODE-MIB", "cpmcBundleFeatures"), ("CISCO-PSA-MICROCODE-MIB", "cpmcNotifEnables"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsaMicrocodeParamsGroup = ciscoPsaMicrocodeParamsGroup.setStatus('current')
ciscoPsaMicrocodeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 2, 2)).setObjects(("CISCO-PSA-MICROCODE-MIB", "ciscoPsaMicrocodeReload"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsaMicrocodeNotifGroup = ciscoPsaMicrocodeNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PSA-MICROCODE-MIB", cpmcModulePsaPrevBundleId=cpmcModulePsaPrevBundleId, cpmcBundleTable=cpmcBundleTable, ciscoPsaMicrocodeParamsGroup=ciscoPsaMicrocodeParamsGroup, cpmcBundleId=cpmcBundleId, ciscoPsaMicrocodeNotifGroup=ciscoPsaMicrocodeNotifGroup, PsaMicrocodeBundleId=PsaMicrocodeBundleId, cpmcModulePsaTable=cpmcModulePsaTable, cpmcNotifEnables=cpmcNotifEnables, ciscoPsaMicrocodeMIB=ciscoPsaMicrocodeMIB, ciscoPsaMicrocodeMIBGroups=ciscoPsaMicrocodeMIBGroups, cpmcBundle=cpmcBundle, PYSNMP_MODULE_ID=ciscoPsaMicrocodeMIB, cpmcBundleFeatures=cpmcBundleFeatures, cpmcModulePsaFeaturesEnabled=cpmcModulePsaFeaturesEnabled, cpmcBundleEntry=cpmcBundleEntry, ciscoPsaMicrocodeReload=ciscoPsaMicrocodeReload, cpmcNotif=cpmcNotif, cpmcModulePsa=cpmcModulePsa, cpmcModulePsaFeaturesDisabled=cpmcModulePsaFeaturesDisabled, ciscoPsaMicrocodeMIBNotifs=ciscoPsaMicrocodeMIBNotifs, ciscoPsaMicrocodeMIBCompliance=ciscoPsaMicrocodeMIBCompliance, cpmcModulePsaCurrBundleId=cpmcModulePsaCurrBundleId, cpmcModulePsaEntry=cpmcModulePsaEntry, ciscoPsaMicrocodeMIBObjects=ciscoPsaMicrocodeMIBObjects, PsaMicrocodeFeatures=PsaMicrocodeFeatures, ciscoPsaMicrocodeMIBCompliances=ciscoPsaMicrocodeMIBCompliances, ciscoPsaMicrocodeMIBConformance=ciscoPsaMicrocodeMIBConformance)
