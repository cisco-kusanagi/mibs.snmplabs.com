#
# PySNMP MIB module CISCO-COPS-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-COPS-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:54:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, Counter64, Counter32, iso, IpAddress, MibIdentifier, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "Counter64", "Counter32", "iso", "IpAddress", "MibIdentifier", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCopsClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 313))
ciscoCopsClientCapability.setRevisions(('2004-03-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCopsClientCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCopsClientCapability.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: ciscoCopsClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCopsClientCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCopsClientCapability.setDescription('The capabilities description of CISCO-COPS-CLIENT-MIB.')
ccopsClientCapCatOSV53R2Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 313, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV53R2Cat6k = ccopsClientCapCatOSV53R2Cat6k.setProductRelease('Cisco CatOS 5.3(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV53R2Cat6k = ccopsClientCapCatOSV53R2Cat6k.setStatus('current')
if mibBuilder.loadTexts: ccopsClientCapCatOSV53R2Cat6k.setDescription('CISCO-COPS-CLIENT-MIB capabilities.')
ccopsClientCapCatOSV61R1Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 313, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV61R1Cat6k = ccopsClientCapCatOSV61R1Cat6k.setProductRelease('Cisco CatOS 6.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV61R1Cat6k = ccopsClientCapCatOSV61R1Cat6k.setStatus('current')
if mibBuilder.loadTexts: ccopsClientCapCatOSV61R1Cat6k.setDescription('CISCO-COPS-CLIENT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-COPS-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=ciscoCopsClientCapability, ccopsClientCapCatOSV61R1Cat6k=ccopsClientCapCatOSV61R1Cat6k, ciscoCopsClientCapability=ciscoCopsClientCapability, ccopsClientCapCatOSV53R2Cat6k=ccopsClientCapCatOSV53R2Cat6k)
