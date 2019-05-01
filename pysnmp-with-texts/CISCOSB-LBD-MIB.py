#
# PySNMP MIB module CISCOSB-LBD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-LBD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:22:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, iso, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, NotificationType, TimeTicks, Counter64, Bits, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "iso", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "NotificationType", "TimeTicks", "Counter64", "Bits", "Gauge32", "Counter32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
rlLbd = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127))
rlLbd.setRevisions(('2007-11-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlLbd.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlLbd.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlLbd.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlLbd.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlLbd.setDescription('The private MIB module definition for Loopback Detection MIB.')
rlLbdEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdEnable.setStatus('current')
if mibBuilder.loadTexts: rlLbdEnable.setDescription('Enable/Disable Loopback Detection in the switch.')
rlLbdDetectionInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdDetectionInterval.setStatus('current')
if mibBuilder.loadTexts: rlLbdDetectionInterval.setDescription('The time in seconds that should pass between unicast LBD packets.')
rlLbdMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("source-mac-addr", 1), ("base-mac-addr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdMode.setStatus('current')
if mibBuilder.loadTexts: rlLbdMode.setDescription('Loopback detection mode.')
rlLbdIfAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdIfAdminStatus.setStatus('current')
if mibBuilder.loadTexts: rlLbdIfAdminStatus.setDescription("Loopback Detection admin status. Each port of the system is represented by a single bit within the value of this object. If that bit has a value of '1' then that port has enabled admin status,; if the port is disabled, its bit has a value of '0'.")
mibBuilder.exportSymbols("CISCOSB-LBD-MIB", rlLbd=rlLbd, rlLbdEnable=rlLbdEnable, PYSNMP_MODULE_ID=rlLbd, rlLbdDetectionInterval=rlLbdDetectionInterval, rlLbdMode=rlLbdMode, rlLbdIfAdminStatus=rlLbdIfAdminStatus)
