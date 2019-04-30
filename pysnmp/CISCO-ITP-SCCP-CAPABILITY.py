#
# PySNMP MIB module CISCO-ITP-SCCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-SCCP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Gauge32, Integer32, iso, Counter64, Unsigned32, IpAddress, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "iso", "Counter64", "Unsigned32", "IpAddress", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpSccpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 221))
ciscoItpSccpCapability.setRevisions(('2002-03-04 00:00', '2001-10-24 00:00',))
if mibBuilder.loadTexts: ciscoItpSccpCapability.setLastUpdated('200203040000Z')
if mibBuilder.loadTexts: ciscoItpSccpCapability.setOrganization('Cisco Systems, Inc.')
ciscoItpSccpCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 221, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R024MB1 = ciscoItpSccpCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R024MB1 = ciscoItpSccpCapabilityV12R024MB1.setStatus('current')
ciscoItpSccpCapabilityV12R0204MB4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 221, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R0204MB4 = ciscoItpSccpCapabilityV12R0204MB4.setProductRelease('Cisco IOS 12.2(4)MB4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R0204MB4 = ciscoItpSccpCapabilityV12R0204MB4.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-SCCP-CAPABILITY", ciscoItpSccpCapability=ciscoItpSccpCapability, ciscoItpSccpCapabilityV12R0204MB4=ciscoItpSccpCapabilityV12R0204MB4, PYSNMP_MODULE_ID=ciscoItpSccpCapability, ciscoItpSccpCapabilityV12R024MB1=ciscoItpSccpCapabilityV12R024MB1)
