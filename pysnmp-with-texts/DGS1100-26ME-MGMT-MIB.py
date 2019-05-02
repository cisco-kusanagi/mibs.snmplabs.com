#
# PySNMP MIB module DGS1100-26ME-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS1100-26ME-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:45:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
dgs1100_26ME, = mibBuilder.importSymbols("DGS1100PRIMGMT-MIB", "dgs1100-26ME")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Gauge32, IpAddress, MibIdentifier, Counter64, NotificationType, ObjectIdentity, Integer32, TimeTicks, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Gauge32", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "ObjectIdentity", "Integer32", "TimeTicks", "Bits", "iso")
DisplayString, RowStatus, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "MacAddress", "TextualConvention")
swL2MgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 134, 12, 12))
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

mibBuilder.exportSymbols("DGS1100-26ME-MGMT-MIB", VlanId=VlanId, VlanIndex=VlanIndex, PortList=PortList, PYSNMP_MODULE_ID=swL2MgmtMIB, swL2MgmtMIB=swL2MgmtMIB)
