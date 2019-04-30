#
# PySNMP MIB module CISCOSB-LBD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-LBD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:06:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Bits, ModuleIdentity, TimeTicks, Counter32, ObjectIdentity, Gauge32, NotificationType, IpAddress, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Bits", "ModuleIdentity", "TimeTicks", "Counter32", "ObjectIdentity", "Gauge32", "NotificationType", "IpAddress", "iso", "Unsigned32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
rlLbd = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127))
rlLbd.setRevisions(('2007-11-07 00:00',))
if mibBuilder.loadTexts: rlLbd.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlLbd.setOrganization('Cisco Small Business')
rlLbdEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdEnable.setStatus('current')
rlLbdDetectionInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdDetectionInterval.setStatus('current')
rlLbdMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("source-mac-addr", 1), ("base-mac-addr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdMode.setStatus('current')
rlLbdIfAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdIfAdminStatus.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-LBD-MIB", rlLbd=rlLbd, rlLbdIfAdminStatus=rlLbdIfAdminStatus, rlLbdMode=rlLbdMode, rlLbdDetectionInterval=rlLbdDetectionInterval, PYSNMP_MODULE_ID=rlLbd, rlLbdEnable=rlLbdEnable)
