#
# PySNMP MIB module CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:04:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Gauge32, IpAddress, Counter32, ModuleIdentity, Unsigned32, Integer32, ObjectIdentity, iso, TimeTicks, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Counter32", "ModuleIdentity", "Unsigned32", "Integer32", "ObjectIdentity", "iso", "TimeTicks", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL2L3IfConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 326))
ciscoL2L3IfConfigCapability.setRevisions(('2014-04-04 00:00', '2013-08-28 00:00', '2004-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setRevisionsDescriptions(('Added ciscoL2L3IfConfigCapNxOSV06R0201PMds agent capability statement.', 'Added ciscoL2L3IfConfigCapNxOSV06R0202PN7K agent capability statement.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setDescription('The agent capabilities description of CISCO-L2L3-INTERFACE-CONFIG-MIB.')
ciscoL2L3IfConfigCapV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapV12R0119E = ciscoL2L3IfConfigCapV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapV12R0119E = ciscoL2L3IfConfigCapV12R0119E.setStatus('current')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapV12R0119E.setDescription('CISCO-L2L3-INTERFACE-CONFIG-MIB agent capabilities.')
ciscoL2L3IfConfigCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0202PN7K = ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on \n                    Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0202PN7K = ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setDescription('CISCO-L2L3-INTERFACE-CONFIG-MIB agent capabilities.')
ciscoL2L3IfConfigCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0201PMds = ciscoL2L3IfConfigCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0201PMds = ciscoL2L3IfConfigCapNxOSV06R0201PMds.setStatus('current')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapNxOSV06R0201PMds.setDescription('CISCO-L2L3-INTERFACE-CONFIG-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY", PYSNMP_MODULE_ID=ciscoL2L3IfConfigCapability, ciscoL2L3IfConfigCapNxOSV06R0201PMds=ciscoL2L3IfConfigCapNxOSV06R0201PMds, ciscoL2L3IfConfigCapNxOSV06R0202PN7K=ciscoL2L3IfConfigCapNxOSV06R0202PN7K, ciscoL2L3IfConfigCapability=ciscoL2L3IfConfigCapability, ciscoL2L3IfConfigCapV12R0119E=ciscoL2L3IfConfigCapV12R0119E)
