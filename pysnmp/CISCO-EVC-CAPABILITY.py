#
# PySNMP MIB module CISCO-EVC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-EVC-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ObjectIdentity, Integer32, Bits, Gauge32, IpAddress, MibIdentifier, iso, Counter32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ObjectIdentity", "Integer32", "Bits", "Gauge32", "IpAddress", "MibIdentifier", "iso", "Counter32", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEvcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 568))
ciscoEvcCapability.setRevisions(('2008-08-26 00:00',))
if mibBuilder.loadTexts: ciscoEvcCapability.setLastUpdated('200808260000Z')
if mibBuilder.loadTexts: ciscoEvcCapability.setOrganization('Cisco Systems, Inc.')
ciscoEvcCapabilityV12R02SR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 568, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02SR = ciscoEvcCapabilityV12R02SR.setProductRelease('Cisco IOS 12.2 SR Release')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02SR = ciscoEvcCapabilityV12R02SR.setStatus('current')
ciscoEvcCapabilityV12R02XO = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 568, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02XO = ciscoEvcCapabilityV12R02XO.setProductRelease('Cisco IOS 12.2 XO Release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02XO = ciscoEvcCapabilityV12R02XO.setStatus('current')
mibBuilder.exportSymbols("CISCO-EVC-CAPABILITY", ciscoEvcCapabilityV12R02XO=ciscoEvcCapabilityV12R02XO, ciscoEvcCapability=ciscoEvcCapability, ciscoEvcCapabilityV12R02SR=ciscoEvcCapabilityV12R02SR, PYSNMP_MODULE_ID=ciscoEvcCapability)
