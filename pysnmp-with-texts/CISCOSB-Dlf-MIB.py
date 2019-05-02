#
# PySNMP MIB module CISCOSB-Dlf-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-Dlf-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:22:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ObjectIdentity, Counter64, Gauge32, ModuleIdentity, Bits, iso, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Counter64", "Gauge32", "ModuleIdentity", "Bits", "iso", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlDlf = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 135))
if mibBuilder.loadTexts: rlDlf.setLastUpdated('200809151234Z')
if mibBuilder.loadTexts: rlDlf.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlDlf.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlDlf.setDescription('The private MIB module definition for DLF Ports MIB. unknown unicast egress filtering ')
rlDlfPortList = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 135, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDlfPortList.setStatus('current')
if mibBuilder.loadTexts: rlDlfPortList.setDescription('A port bitmap containing entries of unknown unicas egress filtering')
mibBuilder.exportSymbols("CISCOSB-Dlf-MIB", rlDlfPortList=rlDlfPortList, PYSNMP_MODULE_ID=rlDlf, rlDlf=rlDlf)
