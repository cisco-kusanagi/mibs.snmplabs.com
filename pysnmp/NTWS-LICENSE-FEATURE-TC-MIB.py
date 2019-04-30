#
# PySNMP MIB module NTWS-LICENSE-FEATURE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-LICENSE-FEATURE-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, Counter32, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Bits, Integer32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "Counter32", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Bits", "Integer32", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsLicenseFeatureTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 19))
ntwsLicenseFeatureTc.setRevisions(('2009-11-16 00:01',))
if mibBuilder.loadTexts: ntwsLicenseFeatureTc.setLastUpdated('200911160001Z')
if mibBuilder.loadTexts: ntwsLicenseFeatureTc.setOrganization('Nortel Networks')
class NtwsLicenseFeature(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("none", 1), ("maxSupportedAPsOrDAPs", 2), ("fips", 11), ("advancedVoice", 12), ("highAvailability", 13), ("maxSupportedHighSpeedMeshBridgingAPs", 14), ("maxSupportedWapiAPs", 15), ("maxSupportedAdvancedLocalSwitchingAPs", 16))

mibBuilder.exportSymbols("NTWS-LICENSE-FEATURE-TC-MIB", ntwsLicenseFeatureTc=ntwsLicenseFeatureTc, NtwsLicenseFeature=NtwsLicenseFeature, PYSNMP_MODULE_ID=ntwsLicenseFeatureTc)
