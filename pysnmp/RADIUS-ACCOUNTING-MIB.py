#
# PySNMP MIB module RADIUS-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADIUS-ACCOUNTING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:36:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, Integer32, Counter32, Gauge32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, IpAddress, NotificationType, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Integer32", "Counter32", "Gauge32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swRadiusAccountMGMTMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 55))
if mibBuilder.loadTexts: swRadiusAccountMGMTMIB.setLastUpdated('0712200000Z')
if mibBuilder.loadTexts: swRadiusAccountMGMTMIB.setOrganization('D-Link Corp.')
radiusAccountCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 55, 1))
accountingShellState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 55, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accountingShellState.setStatus('current')
accountingSystemState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 55, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accountingSystemState.setStatus('current')
accountingNetworkState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 55, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accountingNetworkState.setStatus('current')
mibBuilder.exportSymbols("RADIUS-ACCOUNTING-MIB", swRadiusAccountMGMTMIB=swRadiusAccountMGMTMIB, accountingShellState=accountingShellState, accountingSystemState=accountingSystemState, accountingNetworkState=accountingNetworkState, PYSNMP_MODULE_ID=swRadiusAccountMGMTMIB, radiusAccountCtrl=radiusAccountCtrl)
