#
# PySNMP MIB module RBN-ATM-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-ATM-PROFILE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
atmTrafficDescrParamEntry, = mibBuilder.importSymbols("ATM-MIB", "atmTrafficDescrParamEntry")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Counter64, Unsigned32, MibIdentifier, IpAddress, TimeTicks, ObjectIdentity, Gauge32, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Counter64", "Unsigned32", "MibIdentifier", "IpAddress", "TimeTicks", "ObjectIdentity", "Gauge32", "NotificationType", "Counter32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rbnAtmProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 2))
if mibBuilder.loadTexts: rbnAtmProfileMIB.setLastUpdated('9807151645Z')
if mibBuilder.loadTexts: rbnAtmProfileMIB.setOrganization('RedBack Networks, Inc.')
class AtmProfileName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '80a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 80)

rbnAtmProfileMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1))
rbnAtmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1), )
if mibBuilder.loadTexts: rbnAtmProfileTable.setStatus('current')
rbnAtmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1), )
atmTrafficDescrParamEntry.registerAugmentions(("RBN-ATM-PROFILE-MIB", "rbnAtmProfileEntry"))
rbnAtmProfileEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
if mibBuilder.loadTexts: rbnAtmProfileEntry.setStatus('current')
rbnAtmProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 1), AtmProfileName().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmProfileName.setStatus('current')
rbnAtmCountersEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmCountersEnabled.setStatus('current')
rbnAtmCellLossPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmCellLossPriority.setStatus('current')
rbnAtmTransmitBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmTransmitBuffers.setStatus('current')
rbnAtmProfileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2))
rbnAtmProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 1))
rbnAtmProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 2))
rbnAtmProfileMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 2, 1)).setObjects(("RBN-ATM-PROFILE-MIB", "rbnAtmProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmProfileMIBCompliance = rbnAtmProfileMIBCompliance.setStatus('current')
rbnAtmProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 1, 1)).setObjects(("RBN-ATM-PROFILE-MIB", "rbnAtmProfileName"), ("RBN-ATM-PROFILE-MIB", "rbnAtmCountersEnabled"), ("RBN-ATM-PROFILE-MIB", "rbnAtmCellLossPriority"), ("RBN-ATM-PROFILE-MIB", "rbnAtmTransmitBuffers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmProfileGroup = rbnAtmProfileGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-ATM-PROFILE-MIB", rbnAtmProfileMIBCompliances=rbnAtmProfileMIBCompliances, rbnAtmProfileMIBGroups=rbnAtmProfileMIBGroups, rbnAtmProfileMIBCompliance=rbnAtmProfileMIBCompliance, rbnAtmProfileMIBObjects=rbnAtmProfileMIBObjects, rbnAtmProfileName=rbnAtmProfileName, rbnAtmTransmitBuffers=rbnAtmTransmitBuffers, rbnAtmCellLossPriority=rbnAtmCellLossPriority, AtmProfileName=AtmProfileName, rbnAtmProfileGroup=rbnAtmProfileGroup, rbnAtmProfileMIB=rbnAtmProfileMIB, rbnAtmProfileMIBConformance=rbnAtmProfileMIBConformance, rbnAtmProfileTable=rbnAtmProfileTable, rbnAtmProfileEntry=rbnAtmProfileEntry, PYSNMP_MODULE_ID=rbnAtmProfileMIB, rbnAtmCountersEnabled=rbnAtmCountersEnabled)
