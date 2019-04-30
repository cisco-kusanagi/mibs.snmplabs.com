#
# PySNMP MIB module RBN-X-ATM-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-X-ATM-PROFILE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:45:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
atmTrafficDescrParamEntry, = mibBuilder.importSymbols("ATM-MIB", "atmTrafficDescrParamEntry")
rbnExperiment, = mibBuilder.importSymbols("RBN-SMI", "rbnExperiment")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, iso, ObjectIdentity, MibIdentifier, Counter64, IpAddress, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "iso", "ObjectIdentity", "MibIdentifier", "Counter64", "IpAddress", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnXAtmProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 3, 2))
if mibBuilder.loadTexts: rbnXAtmProfileMIB.setLastUpdated('9807161645Z')
if mibBuilder.loadTexts: rbnXAtmProfileMIB.setOrganization('RedBack Networks, Inc.')
rbnXAtmProfileMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 2, 1))
rbnXAtmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 3, 2, 1, 1), )
if mibBuilder.loadTexts: rbnXAtmProfileTable.setStatus('current')
rbnXAtmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 3, 2, 1, 1, 1), )
atmTrafficDescrParamEntry.registerAugmentions(("RBN-X-ATM-PROFILE-MIB", "rbnXAtmProfileEntry"))
rbnXAtmProfileEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
if mibBuilder.loadTexts: rbnXAtmProfileEntry.setStatus('current')
rbnXAtmServiceCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("cbr", 2), ("rtVbr", 3), ("nrtVbr", 4), ("abr", 5), ("ubr", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnXAtmServiceCategory.setStatus('current')
rbnXAtmProfileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 2, 2))
rbnXAtmProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 2, 2, 1))
rbnXAtmProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 2, 2, 2))
rbnXAtmProfileMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 3, 2, 2, 2, 1)).setObjects(("RBN-X-ATM-PROFILE-MIB", "rbnXAtmProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnXAtmProfileMIBCompliance = rbnXAtmProfileMIBCompliance.setStatus('current')
rbnXAtmProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 3, 2, 2, 1, 1)).setObjects(("RBN-X-ATM-PROFILE-MIB", "rbnXAtmServiceCategory"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnXAtmProfileGroup = rbnXAtmProfileGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-X-ATM-PROFILE-MIB", rbnXAtmProfileEntry=rbnXAtmProfileEntry, rbnXAtmProfileMIB=rbnXAtmProfileMIB, rbnXAtmProfileMIBGroups=rbnXAtmProfileMIBGroups, rbnXAtmServiceCategory=rbnXAtmServiceCategory, rbnXAtmProfileMIBCompliances=rbnXAtmProfileMIBCompliances, PYSNMP_MODULE_ID=rbnXAtmProfileMIB, rbnXAtmProfileMIBConformance=rbnXAtmProfileMIBConformance, rbnXAtmProfileTable=rbnXAtmProfileTable, rbnXAtmProfileMIBCompliance=rbnXAtmProfileMIBCompliance, rbnXAtmProfileGroup=rbnXAtmProfileGroup, rbnXAtmProfileMIBObjects=rbnXAtmProfileMIBObjects)
