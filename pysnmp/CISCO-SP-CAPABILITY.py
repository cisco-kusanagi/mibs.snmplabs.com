#
# PySNMP MIB module CISCO-SP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
NotificationType, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Unsigned32, ModuleIdentity, Integer32, Counter64, IpAddress, Bits, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Integer32", "Counter64", "IpAddress", "Bits", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cSpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 189))
cSpCapability.setRevisions(('2001-06-06 00:00',))
if mibBuilder.loadTexts: cSpCapability.setLastUpdated('200106060000Z')
if mibBuilder.loadTexts: cSpCapability.setOrganization('Cisco Systems, Inc.')
cSpCapabilityV12R021MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 189, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSpCapabilityV12R021MB1 = cSpCapabilityV12R021MB1.setProductRelease('Cisco IOS 12.2(1)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSpCapabilityV12R021MB1 = cSpCapabilityV12R021MB1.setStatus('current')
mibBuilder.exportSymbols("CISCO-SP-CAPABILITY", cSpCapability=cSpCapability, PYSNMP_MODULE_ID=cSpCapability, cSpCapabilityV12R021MB1=cSpCapabilityV12R021MB1)
