#
# PySNMP MIB module TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, NotificationType, Counter32, IpAddress, Integer32, Bits, Unsigned32, ModuleIdentity, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "NotificationType", "Counter32", "IpAddress", "Integer32", "Bits", "Unsigned32", "ModuleIdentity", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzLicenseFeatureTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 19))
trpzLicenseFeatureTc.setRevisions(('2011-01-27 01:00', '2009-11-17 00:20', '2009-11-16 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzLicenseFeatureTc.setRevisionsDescriptions(("v1.0.0: Added two license feature values: 'maxSupportedRemoteOfficeAPs(17)', 'maxSupportedSpectrumAnalysisAPs(18)'. (for 7.5 release)", "v0.2.0: Added license feature value 'maxSupportedSessions(3)' (for 7.3 release)", 'v0.1.1: initial version, for 7.1 release',))
if mibBuilder.loadTexts: trpzLicenseFeatureTc.setLastUpdated('201101270100Z')
if mibBuilder.loadTexts: trpzLicenseFeatureTc.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzLicenseFeatureTc.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzLicenseFeatureTc.setDescription("Textual Convention for the Licensable Features of Trapeze Networks wireless switches. Copyright 2009-2011 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzLicenseFeature(TextualConvention, Integer32):
    description = 'Enumeration of the licensable features.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 11, 12, 13, 14, 16, 17, 18))
    namedValues = NamedValues(("none", 1), ("maxSupportedAPsOrDAPs", 2), ("maxSupportedSessions", 3), ("fips", 11), ("advancedVoice", 12), ("highAvailability", 13), ("maxSupportedHighSpeedMeshBridgingAPs", 14), ("maxSupportedAdvancedLocalSwitchingAPs", 16), ("maxSupportedRemoteOfficeAPs", 17), ("maxSupportedSpectrumAnalysisAPs", 18))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB", trpzLicenseFeatureTc=trpzLicenseFeatureTc, PYSNMP_MODULE_ID=trpzLicenseFeatureTc, TrpzLicenseFeature=TrpzLicenseFeature)
