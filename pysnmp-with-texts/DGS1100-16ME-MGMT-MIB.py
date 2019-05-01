#
# PySNMP MIB module DGS1100-16ME-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS1100-16ME-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:45:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dgs1100_16ME, = mibBuilder.importSymbols("DGS1100PRIMGMT-MIB", "dgs1100-16ME")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, MibIdentifier, NotificationType, IpAddress, Counter64, Counter32, iso, ModuleIdentity, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "MibIdentifier", "NotificationType", "IpAddress", "Counter64", "Counter32", "iso", "ModuleIdentity", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity")
RowStatus, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "DisplayString", "TextualConvention")
swL2MgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 134, 4, 4))
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

mibBuilder.exportSymbols("DGS1100-16ME-MGMT-MIB", PortList=PortList, VlanIndex=VlanIndex, PYSNMP_MODULE_ID=swL2MgmtMIB, swL2MgmtMIB=swL2MgmtMIB, VlanId=VlanId)
