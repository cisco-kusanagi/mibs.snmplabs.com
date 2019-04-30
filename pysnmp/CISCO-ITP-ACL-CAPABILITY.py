#
# PySNMP MIB module CISCO-ITP-ACL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-ACL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, IpAddress, NotificationType, Counter32, Integer32, Counter64, Unsigned32, TimeTicks, Bits, MibIdentifier, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "IpAddress", "NotificationType", "Counter32", "Integer32", "Counter64", "Unsigned32", "TimeTicks", "Bits", "MibIdentifier", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpAclCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 214))
ciscoItpAclCapability.setRevisions(('2001-10-24 00:00',))
if mibBuilder.loadTexts: ciscoItpAclCapability.setLastUpdated('200110240000Z')
if mibBuilder.loadTexts: ciscoItpAclCapability.setOrganization('Cisco Systems, Inc.')
ciscoItpAclCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 214, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpAclCapabilityV12R024MB1 = ciscoItpAclCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpAclCapabilityV12R024MB1 = ciscoItpAclCapabilityV12R024MB1.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-ACL-CAPABILITY", ciscoItpAclCapability=ciscoItpAclCapability, PYSNMP_MODULE_ID=ciscoItpAclCapability, ciscoItpAclCapabilityV12R024MB1=ciscoItpAclCapabilityV12R024MB1)
