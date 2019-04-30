#
# PySNMP MIB module MITEL-TRAPGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-TRAPGROUP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:03:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, Integer32, Counter64, MibIdentifier, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, NotificationType, Unsigned32, TimeTicks, ObjectIdentity, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Integer32", "Counter64", "MibIdentifier", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "NotificationType", "Unsigned32", "TimeTicks", "ObjectIdentity", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitelRouterSnmpTrapGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7))
mitelRouterSnmpTrapGroup.setRevisions(('2003-03-24 10:50', '2002-04-02 00:00',))
if mibBuilder.loadTexts: mitelRouterSnmpTrapGroup.setLastUpdated('200303241050Z')
if mibBuilder.loadTexts: mitelRouterSnmpTrapGroup.setOrganization('MITEL Networks Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelSnmpTrapGlobal = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelSnmpTrapGlobal.setStatus('current')
mitelSnmpTrapControl = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelSnmpTrapControl.setStatus('current')
mibBuilder.exportSymbols("MITEL-TRAPGROUP-MIB", mitelIpNetRouter=mitelIpNetRouter, mitelProprietary=mitelProprietary, mitelSnmpTrapControl=mitelSnmpTrapControl, mitelPropIpNetworking=mitelPropIpNetworking, mitelRouterSnmpTrapGroup=mitelRouterSnmpTrapGroup, PYSNMP_MODULE_ID=mitelRouterSnmpTrapGroup, mitelSnmpTrapGlobal=mitelSnmpTrapGlobal, mitel=mitel)
