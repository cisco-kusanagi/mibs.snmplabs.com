#
# PySNMP MIB module CISCO-VIDEO-SESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VIDEO-SESSION-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:01:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, iso, MibIdentifier, TimeTicks, Counter32, Gauge32, ObjectIdentity, Counter64, IpAddress, Integer32, Unsigned32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "MibIdentifier", "TimeTicks", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "IpAddress", "Integer32", "Unsigned32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVideoSessionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 599))
ciscoVideoSessionCapability.setRevisions(('2011-05-24 00:00', '2010-11-11 00:00',))
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setLastUpdated('201105240000Z')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setOrganization('Cisco Systems, Inc.')
ciscoVideoSessionCapabilityV15R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 599, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV15R01 = ciscoVideoSessionCapabilityV15R01.setProductRelease('OS=IOS\n                     OSVERSION=15.1\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV15R01 = ciscoVideoSessionCapabilityV15R01.setStatus('current')
ciscoVideoSessionCapabilityV152T02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 599, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV152T02 = ciscoVideoSessionCapabilityV152T02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV152T02 = ciscoVideoSessionCapabilityV152T02.setStatus('current')
mibBuilder.exportSymbols("CISCO-VIDEO-SESSION-CAPABILITY", PYSNMP_MODULE_ID=ciscoVideoSessionCapability, ciscoVideoSessionCapabilityV15R01=ciscoVideoSessionCapabilityV15R01, ciscoVideoSessionCapability=ciscoVideoSessionCapability, ciscoVideoSessionCapabilityV152T02=ciscoVideoSessionCapabilityV152T02)
