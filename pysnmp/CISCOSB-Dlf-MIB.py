#
# PySNMP MIB module CISCOSB-Dlf-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-Dlf-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:06:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Unsigned32, NotificationType, Bits, MibIdentifier, Counter64, Gauge32, ObjectIdentity, iso, ModuleIdentity, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Unsigned32", "NotificationType", "Bits", "MibIdentifier", "Counter64", "Gauge32", "ObjectIdentity", "iso", "ModuleIdentity", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlDlf = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 135))
if mibBuilder.loadTexts: rlDlf.setLastUpdated('200809151234Z')
if mibBuilder.loadTexts: rlDlf.setOrganization('Cisco Systems, Inc.')
rlDlfPortList = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 135, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDlfPortList.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-Dlf-MIB", rlDlfPortList=rlDlfPortList, rlDlf=rlDlf, PYSNMP_MODULE_ID=rlDlf)
