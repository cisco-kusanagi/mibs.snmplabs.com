#
# PySNMP MIB module CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibIdentifier, ModuleIdentity, Gauge32, Integer32, Counter32, Unsigned32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Bits, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Gauge32", "Integer32", "Counter32", "Unsigned32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Bits", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIpslaVideoProfileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 605))
ciscoIpslaVideoProfileCapability.setRevisions(('2011-06-01 00:00',))
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setLastUpdated('201106010000Z')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpslaVideoProfileCapabilityV152R02T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 605, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileCapabilityV152R02T = ciscoIpslaVideoProfileCapabilityV152R02T.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileCapabilityV152R02T = ciscoIpslaVideoProfileCapabilityV152R02T.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpslaVideoProfileCapability, ciscoIpslaVideoProfileCapabilityV152R02T=ciscoIpslaVideoProfileCapabilityV152R02T, ciscoIpslaVideoProfileCapability=ciscoIpslaVideoProfileCapability)
