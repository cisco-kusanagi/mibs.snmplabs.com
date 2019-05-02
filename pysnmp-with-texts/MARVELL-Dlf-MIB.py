#
# PySNMP MIB module MARVELL-Dlf-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-Dlf-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:09:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, Counter32, Bits, NotificationType, ObjectIdentity, Gauge32, iso, Integer32, IpAddress, TimeTicks, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Counter32", "Bits", "NotificationType", "ObjectIdentity", "Gauge32", "iso", "Integer32", "IpAddress", "TimeTicks", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlDlf = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 135))
if mibBuilder.loadTexts: rlDlf.setLastUpdated('200809151234Z')
if mibBuilder.loadTexts: rlDlf.setOrganization('MARVELL Semiconductor, Inc.')
if mibBuilder.loadTexts: rlDlf.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlDlf.setDescription('The private MIB module definition for DLF Ports MIB. unknown unicast egress filtering ')
rlDlfPortList = MibScalar((1, 3, 6, 1, 4, 1, 89, 135, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDlfPortList.setStatus('current')
if mibBuilder.loadTexts: rlDlfPortList.setDescription('A port bitmap containing entries of unknown unicas egress filtering')
mibBuilder.exportSymbols("MARVELL-Dlf-MIB", rlDlf=rlDlf, rlDlfPortList=rlDlfPortList, PYSNMP_MODULE_ID=rlDlf)
