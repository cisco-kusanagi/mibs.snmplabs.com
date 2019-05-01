#
# PySNMP MIB module CISCO-LWAPP-SYS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-SYS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:06:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, MibIdentifier, IpAddress, ModuleIdentity, Bits, TimeTicks, Integer32, ObjectIdentity, Counter64, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "IpAddress", "ModuleIdentity", "Bits", "TimeTicks", "Integer32", "ObjectIdentity", "Counter64", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLwappSysCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 3333))
ciscoLwappSysCapability.setRevisions(('2010-08-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappSysCapability.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappSysCapability.setLastUpdated('201008170000Z')
if mibBuilder.loadTexts: ciscoLwappSysCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappSysCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappSysCapability.setDescription('Agent capabilities for CISCO-LWAPP-SYS-MIB.')
ciscoLwappSysCapabilityCUWNSR7V0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 3333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V0 = ciscoLwappSysCapabilityCUWNSR7V0.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.0 for Cisco WLAN controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V0 = ciscoLwappSysCapabilityCUWNSR7V0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappSysCapabilityCUWNSR7V0.setDescription('CISCO-LWAPP-SYS-MIB capabilities')
ciscoLwappSysCapabilityCUWNSR7V2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 3333, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V2 = ciscoLwappSysCapabilityCUWNSR7V2.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.2 for Cisco WLAN controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V2 = ciscoLwappSysCapabilityCUWNSR7V2.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappSysCapabilityCUWNSR7V2.setDescription('CISCO-LWAPP-SYS-MIB capabilities')
mibBuilder.exportSymbols("CISCO-LWAPP-SYS-CAPABILITY", ciscoLwappSysCapabilityCUWNSR7V0=ciscoLwappSysCapabilityCUWNSR7V0, ciscoLwappSysCapabilityCUWNSR7V2=ciscoLwappSysCapabilityCUWNSR7V2, ciscoLwappSysCapability=ciscoLwappSysCapability, PYSNMP_MODULE_ID=ciscoLwappSysCapability)
