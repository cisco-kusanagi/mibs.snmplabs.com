#
# PySNMP MIB module ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:49:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
dot3adAggPortEntry, = mibBuilder.importSymbols("IEEE8023-LAG-MIB", "dot3adAggPortEntry")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, Counter32, MibIdentifier, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, ModuleIdentity, IpAddress, Unsigned32, ObjectIdentity, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibIdentifier", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "ModuleIdentity", "IpAddress", "Unsigned32", "ObjectIdentity", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysIeee8023LagMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35))
etsysIeee8023LagMibExtMIB.setRevisions(('2004-09-03 15:14', '2003-01-31 23:16',))
if mibBuilder.loadTexts: etsysIeee8023LagMibExtMIB.setLastUpdated('200409031514Z')
if mibBuilder.loadTexts: etsysIeee8023LagMibExtMIB.setOrganization('Enterasys Networks, Inc')
etsysIeee8023LagMibExt = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1))
etsysDot3adAggGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 1))
etsysDot3adAggPort = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2))
etsysDot3adAggGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 1, 1), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot3adAggGlobalEnable.setStatus('current')
etsysDot3adAggGlobalFormSinglePortLags = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot3adAggGlobalFormSinglePortLags.setStatus('current')
etsysDot3adAggPortTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2, 1), )
if mibBuilder.loadTexts: etsysDot3adAggPortTable.setStatus('current')
etsysDot3adAggPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2, 1, 1), )
dot3adAggPortEntry.registerAugmentions(("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggPortEntry"))
etsysDot3adAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysDot3adAggPortEntry.setStatus('current')
etsysDot3adAggPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2, 1, 1, 1), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDot3adAggPortEnable.setStatus('current')
etsysIeee8023LagConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2))
etsysIeee8023LagGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1))
etsysIeee8023LagCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 2))
etsysDot3adAggGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1, 1)).setObjects(("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggGlobalEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot3adAggGlobalGroup = etsysDot3adAggGlobalGroup.setStatus('current')
etsysDot3adAggPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1, 2)).setObjects(("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggPortEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot3adAggPortGroup = etsysDot3adAggPortGroup.setStatus('current')
etsysDot3adAggGlobalSinglePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1, 3)).setObjects(("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggGlobalFormSinglePortLags"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDot3adAggGlobalSinglePortGroup = etsysDot3adAggGlobalSinglePortGroup.setStatus('current')
etsysIeee8023LagCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 2, 1)).setObjects(("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggGlobalGroup"), ("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggPortGroup"), ("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggGlobalSinglePortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIeee8023LagCompliance = etsysIeee8023LagCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", etsysDot3adAggGlobalEnable=etsysDot3adAggGlobalEnable, etsysIeee8023LagMibExtMIB=etsysIeee8023LagMibExtMIB, etsysDot3adAggGlobalGroup=etsysDot3adAggGlobalGroup, etsysDot3adAggPortGroup=etsysDot3adAggPortGroup, etsysIeee8023LagCompliances=etsysIeee8023LagCompliances, etsysIeee8023LagMibExt=etsysIeee8023LagMibExt, etsysDot3adAggGlobalSinglePortGroup=etsysDot3adAggGlobalSinglePortGroup, etsysDot3adAggPortEntry=etsysDot3adAggPortEntry, etsysDot3adAggPortEnable=etsysDot3adAggPortEnable, etsysDot3adAggPortTable=etsysDot3adAggPortTable, etsysIeee8023LagCompliance=etsysIeee8023LagCompliance, etsysIeee8023LagConformance=etsysIeee8023LagConformance, etsysIeee8023LagGroups=etsysIeee8023LagGroups, etsysDot3adAggGlobal=etsysDot3adAggGlobal, PYSNMP_MODULE_ID=etsysIeee8023LagMibExtMIB, etsysDot3adAggGlobalFormSinglePortLags=etsysDot3adAggGlobalFormSinglePortLags, etsysDot3adAggPort=etsysDot3adAggPort)
