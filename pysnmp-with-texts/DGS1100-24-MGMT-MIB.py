#
# PySNMP MIB module DGS1100-24-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS1100-24-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:45:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
dgs1100_24, = mibBuilder.importSymbols("DGS1100PRIMGMT-MIB", "dgs1100-24")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Counter64, Bits, iso, MibIdentifier, ObjectIdentity, Counter32, TimeTicks, IpAddress, Integer32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Counter64", "Bits", "iso", "MibIdentifier", "ObjectIdentity", "Counter32", "TimeTicks", "IpAddress", "Integer32", "NotificationType", "Unsigned32")
TextualConvention, MacAddress, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "RowStatus", "DisplayString")
swL2MgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 134, 7, 7))
if mibBuilder.loadTexts: swL2MgmtMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: swL2MgmtMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swL2MgmtMIB.setContactInfo(' D-Link Corporation Postal: No. 289, Sinhu 3rd Rd., Neihu District, Taipei City 114, Taiwan, R.O.C Tel: +886-2-66000123 E-mail: tsd@dlink.com.tw ')
if mibBuilder.loadTexts: swL2MgmtMIB.setDescription('The Structure of Layer 2 Network Management Information for the proprietary enterprise.')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class VlanIndex(Unsigned32):
    pass

class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

mibBuilder.exportSymbols("DGS1100-24-MGMT-MIB", PYSNMP_MODULE_ID=swL2MgmtMIB, VlanIndex=VlanIndex, swL2MgmtMIB=swL2MgmtMIB, VlanId=VlanId, PortList=PortList)
