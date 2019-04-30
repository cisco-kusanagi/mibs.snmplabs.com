#
# PySNMP MIB module CISCO-COPS-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-COPS-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, Bits, Integer32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, iso, IpAddress, NotificationType, ObjectIdentity, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "Integer32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "iso", "IpAddress", "NotificationType", "ObjectIdentity", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCopsClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 313))
ciscoCopsClientCapability.setRevisions(('2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoCopsClientCapability.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: ciscoCopsClientCapability.setOrganization('Cisco Systems, Inc.')
ccopsClientCapCatOSV53R2Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 313, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV53R2Cat6k = ccopsClientCapCatOSV53R2Cat6k.setProductRelease('Cisco CatOS 5.3(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV53R2Cat6k = ccopsClientCapCatOSV53R2Cat6k.setStatus('current')
ccopsClientCapCatOSV61R1Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 313, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV61R1Cat6k = ccopsClientCapCatOSV61R1Cat6k.setProductRelease('Cisco CatOS 6.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV61R1Cat6k = ccopsClientCapCatOSV61R1Cat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-COPS-CLIENT-CAPABILITY", ccopsClientCapCatOSV53R2Cat6k=ccopsClientCapCatOSV53R2Cat6k, PYSNMP_MODULE_ID=ciscoCopsClientCapability, ciscoCopsClientCapability=ciscoCopsClientCapability, ccopsClientCapCatOSV61R1Cat6k=ccopsClientCapCatOSV61R1Cat6k)
