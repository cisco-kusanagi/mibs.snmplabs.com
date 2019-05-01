#
# PySNMP MIB module Dlink-Dlf-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dlink-Dlf-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:58:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, MibIdentifier, Integer32, NotificationType, Counter32, ModuleIdentity, Counter64, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "MibIdentifier", "Integer32", "NotificationType", "Counter32", "ModuleIdentity", "Counter64", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlDlf = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 135))
if mibBuilder.loadTexts: rlDlf.setLastUpdated('200809151234Z')
if mibBuilder.loadTexts: rlDlf.setOrganization('Dlink, Inc.')
if mibBuilder.loadTexts: rlDlf.setContactInfo('www.dlink.com')
if mibBuilder.loadTexts: rlDlf.setDescription('The private MIB module definition for DLF Ports MIB. unknown unicast egress filtering ')
rlDlfPortList = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 135, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDlfPortList.setStatus('current')
if mibBuilder.loadTexts: rlDlfPortList.setDescription('A port bitmap containing entries of unknown unicas egress filtering')
mibBuilder.exportSymbols("Dlink-Dlf-MIB", rlDlfPortList=rlDlfPortList, PYSNMP_MODULE_ID=rlDlf, rlDlf=rlDlf)
