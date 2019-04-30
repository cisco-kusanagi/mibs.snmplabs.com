#
# PySNMP MIB module CISCO-IKE-FLOW-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IKE-FLOW-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, IpAddress, Unsigned32, Bits, Integer32, ObjectIdentity, TimeTicks, Counter32, MibIdentifier, Counter64, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Unsigned32", "Bits", "Integer32", "ObjectIdentity", "TimeTicks", "Counter32", "MibIdentifier", "Counter64", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIkeFlowExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 490))
ciscoIkeFlowExtCapability.setRevisions(('2006-02-02 00:00',))
if mibBuilder.loadTexts: ciscoIkeFlowExtCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIkeFlowExtCapability.setOrganization('Cisco Systems, Inc.')
cIkeFlowExtCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 490, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIkeFlowExtCapSanOSV30R1MDS9000 = cIkeFlowExtCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIkeFlowExtCapSanOSV30R1MDS9000 = cIkeFlowExtCapSanOSV30R1MDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-IKE-FLOW-EXT-CAPABILITY", ciscoIkeFlowExtCapability=ciscoIkeFlowExtCapability, PYSNMP_MODULE_ID=ciscoIkeFlowExtCapability, cIkeFlowExtCapSanOSV30R1MDS9000=cIkeFlowExtCapSanOSV30R1MDS9000)
