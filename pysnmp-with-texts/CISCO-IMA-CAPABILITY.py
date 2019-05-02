#
# PySNMP MIB module CISCO-IMA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IMA-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
MilliSeconds, = mibBuilder.importSymbols("IMA-MIB", "MilliSeconds")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Unsigned32, ModuleIdentity, Counter32, NotificationType, Bits, Counter64, IpAddress, MibIdentifier, Integer32, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Counter32", "NotificationType", "Bits", "Counter64", "IpAddress", "MibIdentifier", "Integer32", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoImaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 257))
ciscoImaCapability.setRevisions(('2002-08-15 00:00', '2002-04-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoImaCapability.setRevisionsDescriptions(('Added ciscoImaAxsmeCapabilityV3R00 for Enhanced ATM Switch Service Module(AXSM-E), and Enhanced Processor Switch Module 1(PXM1E) uplink.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoImaCapability.setLastUpdated('200208150000Z')
if mibBuilder.loadTexts: ciscoImaCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoImaCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoImaCapability.setDescription('This file defines agent capabilities for IMA-MIB.')
ciscoImaAxsmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 257, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaAxsmeCapabilityV3R00 = ciscoImaAxsmeCapabilityV3R00.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaAxsmeCapabilityV3R00 = ciscoImaAxsmeCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoImaAxsmeCapabilityV3R00.setDescription('IMA-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IMA-CAPABILITY", PYSNMP_MODULE_ID=ciscoImaCapability, ciscoImaAxsmeCapabilityV3R00=ciscoImaAxsmeCapabilityV3R00, ciscoImaCapability=ciscoImaCapability)
