#
# PySNMP MIB module NTWS-LICENSE-FEATURE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-LICENSE-FEATURE-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, ObjectIdentity, IpAddress, Gauge32, iso, Unsigned32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "ObjectIdentity", "IpAddress", "Gauge32", "iso", "Unsigned32", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsLicenseFeatureTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 19))
ntwsLicenseFeatureTc.setRevisions(('2009-11-16 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsLicenseFeatureTc.setRevisionsDescriptions(('v0.1.1: initial version',))
if mibBuilder.loadTexts: ntwsLicenseFeatureTc.setLastUpdated('200911160001Z')
if mibBuilder.loadTexts: ntwsLicenseFeatureTc.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsLicenseFeatureTc.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsLicenseFeatureTc.setDescription("Textual Convention for the Licensable Features of Nortel Networks wireless switches. Copyright 2009 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class NtwsLicenseFeature(TextualConvention, Integer32):
    description = 'Enumeration of the licensable features.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("none", 1), ("maxSupportedAPsOrDAPs", 2), ("fips", 11), ("advancedVoice", 12), ("highAvailability", 13), ("maxSupportedHighSpeedMeshBridgingAPs", 14), ("maxSupportedWapiAPs", 15), ("maxSupportedAdvancedLocalSwitchingAPs", 16))

mibBuilder.exportSymbols("NTWS-LICENSE-FEATURE-TC-MIB", NtwsLicenseFeature=NtwsLicenseFeature, PYSNMP_MODULE_ID=ntwsLicenseFeatureTc, ntwsLicenseFeatureTc=ntwsLicenseFeatureTc)
