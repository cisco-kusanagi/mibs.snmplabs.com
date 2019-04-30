#
# PySNMP MIB module CISCO-MOBILE-IP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MOBILE-IP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, ModuleIdentity, Counter32, ObjectIdentity, IpAddress, MibIdentifier, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "ModuleIdentity", "Counter32", "ObjectIdentity", "IpAddress", "MibIdentifier", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMobileIPCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 449))
ciscoMobileIPCapability.setRevisions(('2005-09-09 00:00',))
if mibBuilder.loadTexts: ciscoMobileIPCapability.setLastUpdated('200509090000Z')
if mibBuilder.loadTexts: ciscoMobileIPCapability.setOrganization('Cisco Systems, Inc.')
ciscoMobileIPCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 449, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobileIPCapabilityV12R04 = ciscoMobileIPCapabilityV12R04.setProductRelease('Cisco IOS 12.4(3)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobileIPCapabilityV12R04 = ciscoMobileIPCapabilityV12R04.setStatus('current')
mibBuilder.exportSymbols("CISCO-MOBILE-IP-CAPABILITY", ciscoMobileIPCapability=ciscoMobileIPCapability, ciscoMobileIPCapabilityV12R04=ciscoMobileIPCapabilityV12R04, PYSNMP_MODULE_ID=ciscoMobileIPCapability)
