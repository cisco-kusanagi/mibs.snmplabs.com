#
# PySNMP MIB module CISCO-OTV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OTV-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, ObjectIdentity, iso, IpAddress, TimeTicks, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Unsigned32, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "ObjectIdentity", "iso", "IpAddress", "TimeTicks", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Unsigned32", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoOtvCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 622))
ciscoOtvCapability.setRevisions(('2013-07-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoOtvCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoOtvCapability.setLastUpdated('201307290000Z')
if mibBuilder.loadTexts: ciscoOtvCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoOtvCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoOtvCapability.setDescription('The capabilities description of CISCO-OTV-MIB.')
ciscoOtvCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 622, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtvCapNxOSV06R0202PN7K = ciscoOtvCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtvCapNxOSV06R0202PN7K = ciscoOtvCapNxOSV06R0202PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoOtvCapNxOSV06R0202PN7K.setDescription('CISCO-OTV-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-OTV-CAPABILITY", ciscoOtvCapability=ciscoOtvCapability, PYSNMP_MODULE_ID=ciscoOtvCapability, ciscoOtvCapNxOSV06R0202PN7K=ciscoOtvCapNxOSV06R0202PN7K)
