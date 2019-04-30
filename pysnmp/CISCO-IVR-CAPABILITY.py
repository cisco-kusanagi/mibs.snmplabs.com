#
# PySNMP MIB module CISCO-IVR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IVR-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibIdentifier, Bits, Counter64, TimeTicks, Counter32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, iso, NotificationType, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "Counter64", "TimeTicks", "Counter32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "iso", "NotificationType", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIvrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 491))
ciscoIvrCapability.setRevisions(('2006-02-02 00:00',))
if mibBuilder.loadTexts: ciscoIvrCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIvrCapability.setOrganization('Cisco Systems, Inc.')
ciscoIvrCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 491, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIvrCapSanOSV30R1MDS9000 = ciscoIvrCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIvrCapSanOSV30R1MDS9000 = ciscoIvrCapSanOSV30R1MDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-IVR-CAPABILITY", ciscoIvrCapability=ciscoIvrCapability, PYSNMP_MODULE_ID=ciscoIvrCapability, ciscoIvrCapSanOSV30R1MDS9000=ciscoIvrCapSanOSV30R1MDS9000)
