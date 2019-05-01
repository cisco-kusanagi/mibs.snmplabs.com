#
# PySNMP MIB module CISCO-ENTITY-DIAG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-DIAG-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:56:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Gauge32, TimeTicks, Unsigned32, Counter32, ObjectIdentity, Integer32, iso, Counter64, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Gauge32", "TimeTicks", "Unsigned32", "Counter32", "ObjectIdentity", "Integer32", "iso", "Counter64", "IpAddress", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityDiagTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 584))
ciscoEntityDiagTcMIB.setRevisions(('2009-07-01 00:00', '2006-12-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setRevisionsDescriptions(("Added enumeration 'none' to CeDiagTestIdentifier.", 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setLastUpdated('200907010000Z')
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-online-diag@cisco.com')
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setDescription('This module defines the textual conventions used within Cisco Entity Diag MIB.')
class CeDiagDiagnosticLevel(TextualConvention, Integer32):
    description = "The relative degree of completeness that a test will exercise a physical entity: 'bypass' - indicates that no testing should be performed. 'minimal' - indicates that the physical entity will only execute those tests characterized as minimal tests. 'complete' - indicates that the physical entity will execute those tests characterized as minimal or complete tests."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("bypass", 1), ("minimal", 2), ("complete", 3))

class CeDiagDiagnosticMethod(TextualConvention, Integer32):
    description = "The method used to invoke a diagnostic: 'bootup' - specifies a diagnostic invoked by a physical entity during its boot-up process. 'onDemand' - specifies a diagnostic invoked by a management application or through some other management interface, such as a command console. 'scheduled' - specifies a diagnostic invoked by the job scheduler. 'healthMonitor' - specifies a diagnostic invoked by a health monitor. 'none' - no diagnostic method is invoked."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("bootup", 1), ("onDemand", 2), ("scheduled", 3), ("healthMonitor", 4), ("none", 5))

class CeDiagTestIdentifier(TextualConvention, Unsigned32):
    description = 'An arbitrary positive integer value that uniquely identifies a test.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagErrorIdentifier(TextualConvention, Unsigned32):
    description = 'An arbitrary integer value that uniquely identifies an error code. An error code maps to a message specifying details or a reason why test failed.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagErrorIdentifierOrZero(TextualConvention, Unsigned32):
    description = "An arbitrary integer value that uniquely identifies an error code. An error code maps to a message specifying details or a reason why a test failed. An object having a value of '0' specifies 'no error message'."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CeDiagJobIdentifier(TextualConvention, Unsigned32):
    description = 'An arbitrary non-zero integer value that uniquely identifies a single job with respect to a physical entity.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagPortList(TextualConvention, OctetString):
    description = "The entPhysicalTable contains conceptual rows representing ports, each having a value that uniquely identifies the port relative to its parent physical entity (example: the value of entPhysicalParentRelPos or external labeling of port). This MIB definition assumes that these values are relatively small integers. An OCTET STRING representing a list of ports, in which each bit represents a single port. The bits in the first octet represent ports identified by the integer values 1 through 8, inclusive, The bits in the second octet represent ports identified by the integer values 9 through 16, inclusive, and so forth. Within each octet, the most significant bit of an octet represents the port identified by the lowest integer value, and the least significant bit represents the port identified by the highest integer value. The figure shown below illustrates the format of a port list 8 octets in length. Octet 1 Octet 32 7 6 5 4 3 2 1 0 7 6 5 4 3 2 1 0 +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ | |...| | +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | +- Port 255 | | | | | | | | | | | | | | +--- Port 254 | | | | | | | | | | | | | +----- Port 253 | | | | | | | | | | | | +------- Port 252 | | | | | | | | | | | +--------- Port 251 | | | | | | | | | | +----------- Port 250 | | | | | | | | | +------------- Port 249 | | | | | | | | +--------------- Port 248 | | | | | | | | : | | | | | | | | : | | | | | | | +--------------------- Port 7 | | | | | | +----------------------- Port 6 | | | | | +------------------------- Port 5 | | | | +--------------------------- Port 4 | | | +----------------------------- Port 3 | | +------------------------------- Port 2 | +--------------------------------- Port 1 +----------------------------------- Port 0 An port list of length N, where N < 32, represents a port list for which ports assigned identifiers greater than or equal to N*8 have the value of '0'. A special case is a port list having a length of '0', which represents the empty set (i.e., no ports). Observe that care should be taken to concerning the numbering of ports relative to their parent physical entity. Some implementations base their numbering at '0' and others base their numbering at '1'. To avert any problems introduced by such inconsistencies, the management application should pay attention to the contents of the entPhysicalTable when constructing a port list."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CeDiagTestList(TextualConvention, OctetString):
    description = "For each unique type of physical entity (i.e., for each set of physical entities sharing a unique entPhysicalVendorType OID), there an exists unique test space. Observe that it is not necessary that all the tests within a space be defined. An OCTET STRING represents an test list, in which each bit represents a single test. The bits in the first octet represent tests identified by the integer values 1 through 8, inclusive, The bits in the second octet represent tests identified by the integer values 9 through 16, inclusive, and so forth. Within each octet, the most significant bit of an octet represents the test identified by the lowest integer value, and the least significant bit represents the test identified by the highest integer value. The figure shown below illustrates the format of an test list. Octet 1 Octet 32 7 6 5 4 3 2 1 0 7 6 5 4 3 2 1 0 +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ | |...| | +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | +- Test 255 | | | | | | | | | | | | | | +--- Test 254 | | | | | | | | | | | | | +----- Test 253 | | | | | | | | | | | | +------- Test 252 | | | | | | | | | | | +--------- Test 251 | | | | | | | | | | +----------- Test 250 | | | | | | | | | +------------- Test 249 | | | | | | | | +--------------- Test 248 | | | | | | | | : | | | | | | | | : | | | | | | | +--------------------- Test 7 | | | | | | +----------------------- Test 6 | | | | | +------------------------- Test 5 | | | | +--------------------------- Test 4 | | | +----------------------------- Test 3 | | +------------------------------- Test 2 | +--------------------------------- Test 1 +----------------------------------- Test 0 An test list of length N, where N < 32, represents a test list for which test N*8 through 255 have the value of '0'. A special case is a test list having a length of '0', which represents a test list of all zeros."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CeDiagJobSuite(TextualConvention, Integer32):
    description = "This object indicates the various system predefined test suites a diagnostic job can choose from. 'none' - indicates that there is no job suite specified. 'complete' - indicates that this job will run the complete tests on the physical entity. 'minimal' - indicates that this job will run the minimal tests on the physical entity. 'nonDisruptive' - indicates that this job will run the nonDisruptive tests on the physical entity. 'perPort' - indicates that this job will run the perPort tests on the physical entity."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("complete", 2), ("minimal", 3), ("nonDisruptive", 4), ("perPort", 5))

mibBuilder.exportSymbols("CISCO-ENTITY-DIAG-TC-MIB", CeDiagErrorIdentifierOrZero=CeDiagErrorIdentifierOrZero, CeDiagDiagnosticLevel=CeDiagDiagnosticLevel, CeDiagErrorIdentifier=CeDiagErrorIdentifier, PYSNMP_MODULE_ID=ciscoEntityDiagTcMIB, CeDiagTestList=CeDiagTestList, CeDiagJobSuite=CeDiagJobSuite, CeDiagTestIdentifier=CeDiagTestIdentifier, CeDiagPortList=CeDiagPortList, CeDiagDiagnosticMethod=CeDiagDiagnosticMethod, ciscoEntityDiagTcMIB=ciscoEntityDiagTcMIB, CeDiagJobIdentifier=CeDiagJobIdentifier)
