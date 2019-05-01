#
# PySNMP MIB module HM2-PLATFORM-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-SFLOW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:32:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hm2PlatformMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, Gauge32, IpAddress, ObjectIdentity, ModuleIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, NotificationType, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Gauge32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "NotificationType", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2PlatformSflow = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 59))
hm2PlatformSflow.setRevisions(('2011-10-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hm2PlatformSflow.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hm2PlatformSflow.setLastUpdated('201110120000Z')
if mibBuilder.loadTexts: hm2PlatformSflow.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hm2PlatformSflow.setContactInfo('Postal: Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Phone: +49 7127 140 E-mail: hac.support@belden.com')
if mibBuilder.loadTexts: hm2PlatformSflow.setDescription('The Hirschmann Private Platform2 MIB for SFlow. Copyright (C) 2011. All Rights Reserved.')
hm2AgentFastPathSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 59, 1))
hm2AgentSflowSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 59, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentSflowSourceInterface.setStatus('current')
if mibBuilder.loadTexts: hm2AgentSflowSourceInterface.setDescription('A source-interface selection on an Interface Index (like vlan based routing interface, port based routing interface, loopback interface, tunnel interface). A non-zero value indicates ifIndex for the corresponding interface entry in the ifTable is selected. A zero value indicates source-interface is un-configured.')
mibBuilder.exportSymbols("HM2-PLATFORM-SFLOW-MIB", PYSNMP_MODULE_ID=hm2PlatformSflow, hm2PlatformSflow=hm2PlatformSflow, hm2AgentSflowSourceInterface=hm2AgentSflowSourceInterface, hm2AgentFastPathSflowObjects=hm2AgentFastPathSflowObjects)
