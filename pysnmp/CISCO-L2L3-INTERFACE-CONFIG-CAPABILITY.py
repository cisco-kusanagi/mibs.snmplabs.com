#
# PySNMP MIB module CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Integer32, Gauge32, TimeTicks, MibIdentifier, ObjectIdentity, iso, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Integer32", "Gauge32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "iso", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL2L3IfConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 326))
ciscoL2L3IfConfigCapability.setRevisions(('2014-04-04 00:00', '2013-08-28 00:00', '2004-02-03 00:00',))
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setOrganization('Cisco Systems, Inc.')
ciscoL2L3IfConfigCapV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapV12R0119E = ciscoL2L3IfConfigCapV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapV12R0119E = ciscoL2L3IfConfigCapV12R0119E.setStatus('current')
ciscoL2L3IfConfigCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0202PN7K = ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on \n                    Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0202PN7K = ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setStatus('current')
ciscoL2L3IfConfigCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0201PMds = ciscoL2L3IfConfigCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0201PMds = ciscoL2L3IfConfigCapNxOSV06R0201PMds.setStatus('current')
mibBuilder.exportSymbols("CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY", ciscoL2L3IfConfigCapV12R0119E=ciscoL2L3IfConfigCapV12R0119E, PYSNMP_MODULE_ID=ciscoL2L3IfConfigCapability, ciscoL2L3IfConfigCapNxOSV06R0201PMds=ciscoL2L3IfConfigCapNxOSV06R0201PMds, ciscoL2L3IfConfigCapNxOSV06R0202PN7K=ciscoL2L3IfConfigCapNxOSV06R0202PN7K, ciscoL2L3IfConfigCapability=ciscoL2L3IfConfigCapability)
