#
# PySNMP MIB module CISCO-SP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Gauge32, iso, Counter32, ModuleIdentity, NotificationType, Integer32, Bits, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Gauge32", "iso", "Counter32", "ModuleIdentity", "NotificationType", "Integer32", "Bits", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cSpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 189))
cSpCapability.setRevisions(('2001-06-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cSpCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cSpCapability.setLastUpdated('200106060000Z')
if mibBuilder.loadTexts: cSpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cSpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: cSpCapability.setDescription('Agent capabilities for the CISCO-SP-MIB.')
cSpCapabilityV12R021MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 189, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSpCapabilityV12R021MB1 = cSpCapabilityV12R021MB1.setProductRelease('Cisco IOS 12.2(1)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSpCapabilityV12R021MB1 = cSpCapabilityV12R021MB1.setStatus('current')
if mibBuilder.loadTexts: cSpCapabilityV12R021MB1.setDescription('IOS 12.2(1)MB1 Cisco CISCO-SP-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SP-CAPABILITY", cSpCapabilityV12R021MB1=cSpCapabilityV12R021MB1, cSpCapability=cSpCapability, PYSNMP_MODULE_ID=cSpCapability)
