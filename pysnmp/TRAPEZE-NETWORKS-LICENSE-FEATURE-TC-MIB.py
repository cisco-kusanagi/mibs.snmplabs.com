#
# PySNMP MIB module TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Unsigned32, IpAddress, MibIdentifier, Integer32, Gauge32, Bits, ObjectIdentity, Counter64, Counter32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "Gauge32", "Bits", "ObjectIdentity", "Counter64", "Counter32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzLicenseFeatureTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 19))
trpzLicenseFeatureTc.setRevisions(('2011-01-27 01:00', '2009-11-17 00:20', '2009-11-16 00:01',))
if mibBuilder.loadTexts: trpzLicenseFeatureTc.setLastUpdated('201101270100Z')
if mibBuilder.loadTexts: trpzLicenseFeatureTc.setOrganization('Trapeze Networks')
class TrpzLicenseFeature(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 11, 12, 13, 14, 16, 17, 18))
    namedValues = NamedValues(("none", 1), ("maxSupportedAPsOrDAPs", 2), ("maxSupportedSessions", 3), ("fips", 11), ("advancedVoice", 12), ("highAvailability", 13), ("maxSupportedHighSpeedMeshBridgingAPs", 14), ("maxSupportedAdvancedLocalSwitchingAPs", 16), ("maxSupportedRemoteOfficeAPs", 17), ("maxSupportedSpectrumAnalysisAPs", 18))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB", trpzLicenseFeatureTc=trpzLicenseFeatureTc, PYSNMP_MODULE_ID=trpzLicenseFeatureTc, TrpzLicenseFeature=TrpzLicenseFeature)
