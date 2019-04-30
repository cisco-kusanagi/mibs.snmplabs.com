#
# PySNMP MIB module CISCO-ITP-SP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-SP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, Counter64, TimeTicks, Unsigned32, IpAddress, Bits, Gauge32, MibIdentifier, NotificationType, Integer32, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "TimeTicks", "Unsigned32", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpSpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 217))
ciscoItpSpCapability.setRevisions(('2002-01-21 00:00', '2001-10-24 00:00',))
if mibBuilder.loadTexts: ciscoItpSpCapability.setLastUpdated('200201210000Z')
if mibBuilder.loadTexts: ciscoItpSpCapability.setOrganization('Cisco Systems, Inc.')
ciscoItpSpCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 217, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R024MB1 = ciscoItpSpCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R024MB1 = ciscoItpSpCapabilityV12R024MB1.setStatus('current')
ciscoItpSpCapabilityV12R0204MB3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 217, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R0204MB3 = ciscoItpSpCapabilityV12R0204MB3.setProductRelease('Cisco IOS 12.2(4)MB3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R0204MB3 = ciscoItpSpCapabilityV12R0204MB3.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-SP-CAPABILITY", ciscoItpSpCapabilityV12R0204MB3=ciscoItpSpCapabilityV12R0204MB3, ciscoItpSpCapability=ciscoItpSpCapability, ciscoItpSpCapabilityV12R024MB1=ciscoItpSpCapabilityV12R024MB1, PYSNMP_MODULE_ID=ciscoItpSpCapability)
