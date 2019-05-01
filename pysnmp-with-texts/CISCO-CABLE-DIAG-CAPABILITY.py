#
# PySNMP MIB module CISCO-CABLE-DIAG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CABLE-DIAG-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:51:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ObjectIdentity, Gauge32, Counter64, Unsigned32, NotificationType, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, MibIdentifier, Counter32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Counter64", "Unsigned32", "NotificationType", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "MibIdentifier", "Counter32", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCableDiagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 394))
ciscoCableDiagCapability.setRevisions(('2004-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableDiagCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCableDiagCapability.setLastUpdated('200402030000Z')
if mibBuilder.loadTexts: ciscoCableDiagCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableDiagCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCableDiagCapability.setDescription('The agent capabilities description of CISCO-CABLE-DIAG-MIB.')
ciscoCableDiagCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 394, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableDiagCapCatOSV08R0301 = ciscoCableDiagCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableDiagCapCatOSV08R0301 = ciscoCableDiagCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoCableDiagCapCatOSV08R0301.setDescription('CISCO-CABLE-DIAG-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-CABLE-DIAG-CAPABILITY", ciscoCableDiagCapability=ciscoCableDiagCapability, PYSNMP_MODULE_ID=ciscoCableDiagCapability, ciscoCableDiagCapCatOSV08R0301=ciscoCableDiagCapCatOSV08R0301)
