#
# PySNMP MIB module CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, ObjectIdentity, NotificationType, Unsigned32, IpAddress, Counter32, TimeTicks, Integer32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "TimeTicks", "Integer32", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoTelepresenceExchangeSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 615))
ciscoTelepresenceExchangeSystemCapability.setRevisions(('2013-04-11 00:00', '2012-08-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setRevisionsDescriptions(('Added ciscoTelepresenceCapabilityCTXV130 capabilities for CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setLastUpdated('201304150000Z')
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-txbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setDescription('Agent capabilities for CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB')
ciscoTelepresenceCapabilityCTXV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 615, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV120 = ciscoTelepresenceCapabilityCTXV120.setProductRelease('OS=TELEPRESENCE EXCHANGE SYSTEM\n                     OSVERSION=1.2.0\n                     PLATFORM=TelePresence (TP)\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV120 = ciscoTelepresenceCapabilityCTXV120.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCapabilityCTXV120.setDescription('TELEPRESENCE EXCHANGE SYSTEM MIB Capabilities')
ciscoTelepresenceCapabilityCTXV130 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 615, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV130 = ciscoTelepresenceCapabilityCTXV130.setProductRelease('OS=TELEPRESENCE EXCHANGE SYSTEM\n                     OSVERSION=1.3.0\n                     PLATFORM=TelePresence (TP)\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV130 = ciscoTelepresenceCapabilityCTXV130.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCapabilityCTXV130.setDescription('TELEPRESENCE EXCHANGE SYSTEM MIB Capabilities')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY", PYSNMP_MODULE_ID=ciscoTelepresenceExchangeSystemCapability, ciscoTelepresenceExchangeSystemCapability=ciscoTelepresenceExchangeSystemCapability, ciscoTelepresenceCapabilityCTXV120=ciscoTelepresenceCapabilityCTXV120, ciscoTelepresenceCapabilityCTXV130=ciscoTelepresenceCapabilityCTXV130)
