#
# PySNMP MIB module CISCO-ITP-ACT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-ACT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, MibIdentifier, Counter32, TimeTicks, ObjectIdentity, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Counter64, Gauge32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Counter32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Counter64", "Gauge32", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpActCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 219))
ciscoItpActCapability.setRevisions(('2001-10-24 00:00',))
if mibBuilder.loadTexts: ciscoItpActCapability.setLastUpdated('200110240000Z')
if mibBuilder.loadTexts: ciscoItpActCapability.setOrganization('Cisco Systems, Inc.')
ciscoItpActCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 219, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpActCapabilityV12R024MB1 = ciscoItpActCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpActCapabilityV12R024MB1 = ciscoItpActCapabilityV12R024MB1.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-ACT-CAPABILITY", ciscoItpActCapabilityV12R024MB1=ciscoItpActCapabilityV12R024MB1, ciscoItpActCapability=ciscoItpActCapability, PYSNMP_MODULE_ID=ciscoItpActCapability)
