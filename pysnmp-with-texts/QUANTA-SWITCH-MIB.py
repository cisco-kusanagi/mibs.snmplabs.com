#
# PySNMP MIB module QUANTA-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QUANTA-SWITCH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:38:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Unsigned32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Bits, ModuleIdentity, Integer32, MibIdentifier, enterprises, ObjectIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Bits", "ModuleIdentity", "Integer32", "MibIdentifier", "enterprises", "ObjectIdentity", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
quanta = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244))
if mibBuilder.loadTexts: quanta.setLastUpdated('200405240000Z')
if mibBuilder.loadTexts: quanta.setOrganization('Quanta Computer Inc.')
if mibBuilder.loadTexts: quanta.setContactInfo(' Customer Support Postal: Quanta Computer Inc. 4, Wen Ming 1 St., Kuei Shan Hsiang, Tao Yuan Shien, Taiwan, R.O.C. Tel: +886 3 328 0050 E-Mail: strong.chen@quantatw.com')
if mibBuilder.loadTexts: quanta.setDescription('first created')
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2))
class AgentPortMask(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0' When setting this value, the system will ignore configuration for ports not between the first and last valid ports. Configuration of any port numbers between this range that are not valid ports return a failure message, but will still apply configuration for valid ports."
    status = 'current'

mibBuilder.exportSymbols("QUANTA-SWITCH-MIB", AgentPortMask=AgentPortMask, switch=switch, PYSNMP_MODULE_ID=quanta, quanta=quanta)
