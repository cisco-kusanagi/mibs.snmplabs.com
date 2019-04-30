#
# PySNMP MIB module CISCO-DIST-DIRECTOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DIST-DIRECTOR-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, ObjectIdentity, Counter64, Unsigned32, NotificationType, MibIdentifier, Gauge32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Counter64", "Unsigned32", "NotificationType", "MibIdentifier", "Gauge32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDistDirCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 267))
ciscoDistDirCapability.setRevisions(('2002-04-23 00:00',))
if mibBuilder.loadTexts: ciscoDistDirCapability.setLastUpdated('200204230000Z')
if mibBuilder.loadTexts: ciscoDistDirCapability.setOrganization('Cisco Systems, Inc.')
ciscoDistDirCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 267, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDistDirCapabilityV12R02 = ciscoDistDirCapabilityV12R02.setProductRelease('Cisco IOS 12.2(8)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDistDirCapabilityV12R02 = ciscoDistDirCapabilityV12R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-DIST-DIRECTOR-CAPABILITY", ciscoDistDirCapabilityV12R02=ciscoDistDirCapabilityV12R02, ciscoDistDirCapability=ciscoDistDirCapability, PYSNMP_MODULE_ID=ciscoDistDirCapability)
