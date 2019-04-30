#
# PySNMP MIB module HM2-PLATFORM-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-SFLOW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hm2PlatformMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Unsigned32, MibIdentifier, IpAddress, TimeTicks, Counter32, Counter64, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "IpAddress", "TimeTicks", "Counter32", "Counter64", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hm2PlatformSflow = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 59))
hm2PlatformSflow.setRevisions(('2011-10-12 00:00',))
if mibBuilder.loadTexts: hm2PlatformSflow.setLastUpdated('201110120000Z')
if mibBuilder.loadTexts: hm2PlatformSflow.setOrganization('Hirschmann Automation and Control GmbH')
hm2AgentFastPathSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 59, 1))
hm2AgentSflowSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 59, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentSflowSourceInterface.setStatus('current')
mibBuilder.exportSymbols("HM2-PLATFORM-SFLOW-MIB", PYSNMP_MODULE_ID=hm2PlatformSflow, hm2PlatformSflow=hm2PlatformSflow, hm2AgentFastPathSflowObjects=hm2AgentFastPathSflowObjects, hm2AgentSflowSourceInterface=hm2AgentSflowSourceInterface)
