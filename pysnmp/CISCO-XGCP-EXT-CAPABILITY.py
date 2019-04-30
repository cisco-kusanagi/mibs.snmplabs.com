#
# PySNMP MIB module CISCO-XGCP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-XGCP-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:05:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Unsigned32, NotificationType, iso, Integer32, MibIdentifier, Bits, ModuleIdentity, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "iso", "Integer32", "MibIdentifier", "Bits", "ModuleIdentity", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoXgcpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoXgcpExtCapability.setRevisions(('2004-06-18 00:00',))
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setLastUpdated('200406180000Z')
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoXgcpExtCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpExtCapabilityV12R03 = ciscoXgcpExtCapabilityV12R03.setProductRelease('Cisco IOS 12.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpExtCapabilityV12R03 = ciscoXgcpExtCapabilityV12R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-XGCP-EXT-CAPABILITY", ciscoXgcpExtCapability=ciscoXgcpExtCapability, PYSNMP_MODULE_ID=ciscoXgcpExtCapability, ciscoXgcpExtCapabilityV12R03=ciscoXgcpExtCapabilityV12R03)
