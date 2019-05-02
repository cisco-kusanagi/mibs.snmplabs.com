#
# PySNMP MIB module FSM7326-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSM7326-REF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, TimeTicks, Gauge32, Integer32, Counter32, Counter64, ModuleIdentity, enterprises, Unsigned32, ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "TimeTicks", "Gauge32", "Integer32", "Counter32", "Counter64", "ModuleIdentity", "enterprises", "Unsigned32", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netgear = MibIdentifier((1, 3, 6, 1, 4, 1, 4526))
snmpManagedSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1))
fsm7326 = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 9))
fsm7326.setRevisions(('2003-05-06 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fsm7326.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: fsm7326.setLastUpdated('200311101200Z')
if mibBuilder.loadTexts: fsm7326.setOrganization('Netgear')
if mibBuilder.loadTexts: fsm7326.setContactInfo('')
if mibBuilder.loadTexts: fsm7326.setDescription('')
class AgentPortMask(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0' When setting this value, the system will ignore configuration for ports not between the first and last valid ports. Configuration of any port numbers between this range that are not valid ports return a failure message, but will still apply configuration for valid ports."
    status = 'current'

mibBuilder.exportSymbols("FSM7326-REF-MIB", snmpManagedSwitch=snmpManagedSwitch, netgear=netgear, fsm7326=fsm7326, PYSNMP_MODULE_ID=fsm7326, AgentPortMask=AgentPortMask)
