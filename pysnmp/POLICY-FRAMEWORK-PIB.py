#
# PySNMP MIB module POLICY-FRAMEWORK-PIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/POLICY-FRAMEWORK-PIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, NotificationType, Counter64, ModuleIdentity, Gauge32, iso, TimeTicks, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "NotificationType", "Counter64", "ModuleIdentity", "Gauge32", "iso", "TimeTicks", "Unsigned32", "MibIdentifier")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
policy, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "policy")
policyFrameworkPib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 4, 1))
policyFrameworkPib.setRevisions(('2004-07-20 00:00',))
if mibBuilder.loadTexts: policyFrameworkPib.setLastUpdated('200407200000Z')
if mibBuilder.loadTexts: policyFrameworkPib.setOrganization('IETF RAP WG')
policyBasePibClass = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 1, 1))
class Role(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class RoleCombination(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PolicyInstanceId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

policyPrcSupportTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1), )
if mibBuilder.loadTexts: policyPrcSupportTable.setStatus('current')
policyPrcSupportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1), ).setIndexNames((0, "POLICY-FRAMEWORK-PIB", "policyPrcSupportPrid"))
if mibBuilder.loadTexts: policyPrcSupportEntry.setStatus('current')
policyPrcSupportPrid = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: policyPrcSupportPrid.setStatus('current')
policyPrcSupportSupportedPrc = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyPrcSupportSupportedPrc.setStatus('current')
policyPrcSupportSupportedAttrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyPrcSupportSupportedAttrs.setStatus('current')
policyPrcSupportMaxPris = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyPrcSupportMaxPris.setStatus('current')
policyPibIncarnationTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2), )
if mibBuilder.loadTexts: policyPibIncarnationTable.setStatus('current')
policyPibIncarnationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1), ).setIndexNames((0, "POLICY-FRAMEWORK-PIB", "policyPibIncarnationPrid"))
if mibBuilder.loadTexts: policyPibIncarnationEntry.setStatus('current')
policyPibIncarnationPrid = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: policyPibIncarnationPrid.setStatus('current')
policyPibIncarnationName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyPibIncarnationName.setStatus('current')
policyPibIncarnationId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyPibIncarnationId.setStatus('current')
policyPibIncarnationLongevity = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("expireNever", 1), ("expireImmediate", 2), ("expireOnTimeout", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyPibIncarnationLongevity.setStatus('current')
policyPibIncarnationTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyPibIncarnationTtl.setStatus('current')
policyPibIncarnationActive = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyPibIncarnationActive.setStatus('current')
policyDeviceIdentificationTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3), )
if mibBuilder.loadTexts: policyDeviceIdentificationTable.setStatus('current')
policyDeviceIdentificationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1), ).setIndexNames((0, "POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationPrid"))
if mibBuilder.loadTexts: policyDeviceIdentificationEntry.setStatus('current')
policyDeviceIdentificationPrid = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: policyDeviceIdentificationPrid.setStatus('current')
policyDeviceIdentificationDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyDeviceIdentificationDescr.setStatus('current')
policyDeviceIdentificationMaxMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyDeviceIdentificationMaxMsg.setStatus('current')
policyCompLimitsTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4), )
if mibBuilder.loadTexts: policyCompLimitsTable.setStatus('current')
policyCompLimitsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1), ).setIndexNames((0, "POLICY-FRAMEWORK-PIB", "policyCompLimitsPrid"))
if mibBuilder.loadTexts: policyCompLimitsEntry.setStatus('current')
policyCompLimitsPrid = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: policyCompLimitsPrid.setStatus('current')
policyCompLimitsComponent = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyCompLimitsComponent.setStatus('current')
policyCompLimitsType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyCompLimitsType.setStatus('current')
policyCompLimitsGuidance = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyCompLimitsGuidance.setStatus('current')
policyBasePibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 1, 2))
policyBasePibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 1))
policyBasePibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2))
policyBasePibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 1, 1)).setObjects(("POLICY-FRAMEWORK-PIB", "policyPrcSupportGroup"), ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationGroup"), ("POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationGroup"), ("POLICY-FRAMEWORK-PIB", "policyCompLimitsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyBasePibCompliance = policyBasePibCompliance.setStatus('current')
policyPrcSupportGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 1)).setObjects(("POLICY-FRAMEWORK-PIB", "policyPrcSupportSupportedPrc"), ("POLICY-FRAMEWORK-PIB", "policyPrcSupportSupportedAttrs"), ("POLICY-FRAMEWORK-PIB", "policyPrcSupportMaxPris"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyPrcSupportGroup = policyPrcSupportGroup.setStatus('current')
policyPibIncarnationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 2)).setObjects(("POLICY-FRAMEWORK-PIB", "policyPibIncarnationName"), ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationId"), ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationLongevity"), ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationTtl"), ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationActive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyPibIncarnationGroup = policyPibIncarnationGroup.setStatus('current')
policyDeviceIdentificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 3)).setObjects(("POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationDescr"), ("POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationMaxMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyDeviceIdentificationGroup = policyDeviceIdentificationGroup.setStatus('current')
policyCompLimitsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 4)).setObjects(("POLICY-FRAMEWORK-PIB", "policyCompLimitsComponent"), ("POLICY-FRAMEWORK-PIB", "policyCompLimitsType"), ("POLICY-FRAMEWORK-PIB", "policyCompLimitsGuidance"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyCompLimitsGroup = policyCompLimitsGroup.setStatus('current')
mibBuilder.exportSymbols("POLICY-FRAMEWORK-PIB", policyCompLimitsType=policyCompLimitsType, policyPibIncarnationTable=policyPibIncarnationTable, policyCompLimitsComponent=policyCompLimitsComponent, policyDeviceIdentificationDescr=policyDeviceIdentificationDescr, policyPibIncarnationName=policyPibIncarnationName, policyCompLimitsGroup=policyCompLimitsGroup, policyPibIncarnationPrid=policyPibIncarnationPrid, policyPrcSupportSupportedPrc=policyPrcSupportSupportedPrc, PYSNMP_MODULE_ID=policyFrameworkPib, policyPibIncarnationTtl=policyPibIncarnationTtl, policyPrcSupportSupportedAttrs=policyPrcSupportSupportedAttrs, policyCompLimitsGuidance=policyCompLimitsGuidance, policyDeviceIdentificationGroup=policyDeviceIdentificationGroup, policyPibIncarnationEntry=policyPibIncarnationEntry, policyBasePibCompliances=policyBasePibCompliances, policyCompLimitsEntry=policyCompLimitsEntry, policyDeviceIdentificationTable=policyDeviceIdentificationTable, policyPibIncarnationGroup=policyPibIncarnationGroup, policyBasePibConformance=policyBasePibConformance, policyBasePibGroups=policyBasePibGroups, PolicyInstanceId=PolicyInstanceId, policyPrcSupportPrid=policyPrcSupportPrid, policyDeviceIdentificationPrid=policyDeviceIdentificationPrid, policyPibIncarnationLongevity=policyPibIncarnationLongevity, policyDeviceIdentificationMaxMsg=policyDeviceIdentificationMaxMsg, policyDeviceIdentificationEntry=policyDeviceIdentificationEntry, policyCompLimitsPrid=policyCompLimitsPrid, policyCompLimitsTable=policyCompLimitsTable, policyPrcSupportGroup=policyPrcSupportGroup, policyPrcSupportMaxPris=policyPrcSupportMaxPris, policyPrcSupportEntry=policyPrcSupportEntry, policyBasePibClass=policyBasePibClass, policyBasePibCompliance=policyBasePibCompliance, policyPibIncarnationId=policyPibIncarnationId, policyPrcSupportTable=policyPrcSupportTable, Role=Role, RoleCombination=RoleCombination, policyFrameworkPib=policyFrameworkPib, policyPibIncarnationActive=policyPibIncarnationActive)
