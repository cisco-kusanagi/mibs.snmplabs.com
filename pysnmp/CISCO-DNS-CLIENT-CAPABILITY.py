#
# PySNMP MIB module CISCO-DNS-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DNS-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
IpAddress, NotificationType, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Counter32, ModuleIdentity, iso, TimeTicks, Unsigned32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Counter32", "ModuleIdentity", "iso", "TimeTicks", "Unsigned32", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDNSClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 888))
ciscoDNSClientCapability.setRevisions(('2004-11-25 00:00', '2004-08-10 00:00',))
if mibBuilder.loadTexts: ciscoDNSClientCapability.setLastUpdated('200411250000Z')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setOrganization('Cisco Systems, Inc.')
cDNSClientCapSanOSV20R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 888, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDNSClientCapSanOSV20R1MDS9000 = cDNSClientCapSanOSV20R1MDS9000.setProductRelease('Cisco SanOS 2.0(1) on Cisco MDS 9000\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDNSClientCapSanOSV20R1MDS9000 = cDNSClientCapSanOSV20R1MDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-DNS-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDNSClientCapability, cDNSClientCapSanOSV20R1MDS9000=cDNSClientCapSanOSV20R1MDS9000, ciscoDNSClientCapability=ciscoDNSClientCapability)
