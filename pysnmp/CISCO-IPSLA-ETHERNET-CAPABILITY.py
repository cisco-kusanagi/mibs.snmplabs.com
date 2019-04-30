#
# PySNMP MIB module CISCO-IPSLA-ETHERNET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSLA-ETHERNET-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Unsigned32, Gauge32, Counter32, IpAddress, MibIdentifier, Counter64, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Unsigned32", "Gauge32", "Counter32", "IpAddress", "MibIdentifier", "Counter64", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpSlaEthernetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 498))
ciscoIpSlaEthernetCapability.setRevisions(('2006-02-08 00:00',))
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setLastUpdated('200602080000Z')
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpSlaEthernetCapabilityRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 498, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaEthernetCapabilityRev1 = ciscoIpSlaEthernetCapabilityRev1.setProductRelease('Cisco IOS 12.2(01)SRB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaEthernetCapabilityRev1 = ciscoIpSlaEthernetCapabilityRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPSLA-ETHERNET-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpSlaEthernetCapability, ciscoIpSlaEthernetCapabilityRev1=ciscoIpSlaEthernetCapabilityRev1, ciscoIpSlaEthernetCapability=ciscoIpSlaEthernetCapability)
